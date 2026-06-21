import os
import uuid
from typing import Optional

import cloudinary
import cloudinary.uploader
from fastapi import UploadFile
from starlette.concurrency import run_in_threadpool

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True,
)

CLOUDINARY_FOLDER = os.getenv("CLOUDINARY_FOLDER", "laudo_cards")


async def upload_file_to_cloudinary(file: UploadFile) -> Optional[str]:
    """Upload an image to Cloudinary and return its secure URL (None on failure)."""
    public_id = uuid.uuid4().hex
    try:
        # cloudinary.uploader.upload is blocking (network I/O); keep the event loop free.
        result = await run_in_threadpool(
            cloudinary.uploader.upload,
            file.file,
            folder=CLOUDINARY_FOLDER,
            public_id=public_id,
            resource_type="image",
            overwrite=True,
        )
        return result.get("secure_url")
    except Exception as e:
        print(f"Failed to upload to Cloudinary: {e}")
        return None
