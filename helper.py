import sys
import hashlib
import time
import os
import subprocess
import json
import cv2
try:
    from pyzbar.pyzbar import decode
except ImportError:
    decode = None

# Load .env manually to avoid another dependency
env_vars = {}
try:
    with open('.env') as f:
        for line in f:
            if '=' in line:
                key, val = line.strip().split('=', 1)
                env_vars[key] = val
except FileNotFoundError:
    print("Error: .env file not found")
    sys.exit(1)

CLOUD_NAME = env_vars.get('CLOUDINARY_ENV')
API_KEY = env_vars.get('CLOUDINARY_API_KEY')
API_SECRET = env_vars.get('CLOUDINARY_API_SECRET')

def generate_signature(timestamp):
    to_sign = f"timestamp={timestamp}{API_SECRET}"
    return hashlib.sha1(to_sign.encode('utf-8')).hexdigest()

def upload_image(file_path):
    timestamp = str(int(time.time()))
    signature = generate_signature(timestamp)

    # Resize image if too large (temp file)
    temp_path = file_path + ".min.jpg"
    try:
        img = cv2.imread(file_path)
        if img is None:
            print(f"Could not read image for resizing: {file_path}")
            return None

        # Resize to max dimension 1500px to ensure <10MB
        height, width = img.shape[:2]
        max_dim = 1500
        if max(height, width) > max_dim:
            scale = max_dim / max(height, width)
            new_width = int(width * scale)
            new_height = int(height * scale)
            img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

        cv2.imwrite(temp_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
        upload_path = temp_path
    except Exception as e:
        print(f"Error resizing: {e}")
        upload_path = file_path # Try original if resize fails

    cmd = [
        'curl', '-X', 'POST',
        f'https://api.cloudinary.com/v1_1/{CLOUD_NAME}/image/upload',
        '-F', f'file=@{upload_path}',
        '-F', f'api_key={API_KEY}',
        '-F', f'timestamp={timestamp}',
        '-F', f'signature={signature}'
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        # Cleanup temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)

        response = json.loads(result.stdout)
        if 'secure_url' in response:
            return response['secure_url']
        else:
            print(f"Upload failed: {response}")
            return None
    except Exception as e:
        print(f"Error executing curl: {e}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return None

def read_qr_code(image_path):
    print(f"Reading QR from: {image_path}")
    img = cv2.imread(image_path)
    if img is None:
        print(f"Could not read image: {image_path}")
        return None

    # crop top 30% where QR usually is on slabs
    height, width = img.shape[:2]
    crop_height = int(height * 0.30)
    img_crop = img[0:crop_height, 0:width]

    # Try pyzbar first if available
    if decode:
        print("Trying pyzbar...")
        try:
            # Try on original crop
            decoded_objects = decode(img_crop)
            for obj in decoded_objects:
                return obj.data.decode('utf-8')

            # Try on grayscale
            gray = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
            decoded_objects = decode(gray)
            for obj in decoded_objects:
                return obj.data.decode('utf-8')

            # Try on threshold
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            decoded_objects = decode(thresh)
            for obj in decoded_objects:
                return obj.data.decode('utf-8')
        except Exception as e:
            print(f"pyzbar error: {e}")

    # Fallback to OpenCV QRCodeDetector
    print("Trying cv2.QRCodeDetector...")
    try:
        qr_decoder = cv2.QRCodeDetector()

        # Try on crop
        data, bbox, _ = qr_decoder.detectAndDecode(img_crop)
        if data:
            return data

        # Try on grayscale crop
        gray = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
        data, bbox, _ = qr_decoder.detectAndDecode(gray)
        if data:
            return data

        # Try on threshold
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        data, bbox, _ = qr_decoder.detectAndDecode(thresh)
        if data:
            return data

    except Exception as e:
         print(f"cv2 error: {e}")

    print("No QR found")
    return None

import pytesseract

def get_text(image_path):
    try:
        # Preprocessing for better OCR
        img = cv2.imread(image_path)
        if img is None:
             print(f"Could not read image: {image_path}")
             return None

        print(f"Image shape: {img.shape}")

        # Crop top 25% for label reading (GBA labels are at top)
        height, width = img.shape[:2]
        crop_height = int(height * 0.25)
        img = img[0:crop_height, 0:width]

        # Resize if too large
        height, width = img.shape[:2]
        if height > 1000: # Smaller threshold for cropped header
             scale = 1000 / height
             img = cv2.resize(img, None, fx=scale, fy=scale)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Binary thresholding might be better than Otsu for text on white label
        # _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
        # stick with Otsu for now but maybe invert if text is white on black?
        # GBA label is usually black text on white or metallic.
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(thresh, config=custom_config)

        return text.strip()

    except Exception as e:
        print(f"Error OCR: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python helper.py [upload|qr|ocr] [file_path]")
        sys.exit(1)

    action = sys.argv[1]
    file_path = sys.argv[2]

    if action == "upload":
        url = upload_image(file_path)
        if url:
            print(f"URL:{url}")
    elif action == "qr":
        data = read_qr_code(file_path)
        if data:
            print(f"QR:{data}")
        else:
            print("QR:None")
    elif action == "ocr":
        text = get_text(file_path)
        if text:
            print("---START OCR---")
            print(text)
            print("---END OCR---")
        else:
            print("OCR:None")
