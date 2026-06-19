import os
import boto3
from botocore.exceptions import ClientError
from fastapi import UploadFile

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "http://localhost:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin")
MINIO_BUCKET = os.getenv("MINIO_BUCKET", "laudo-cards")

s3_client = boto3.client(
    's3',
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY,
    region_name='us-east-1' # Default for minio
)

def ensure_bucket_exists():
    try:
        s3_client.head_bucket(Bucket=MINIO_BUCKET)
    except ClientError:
        try:
            s3_client.create_bucket(Bucket=MINIO_BUCKET)
            # Set public read policy for the bucket so frontend can load images
            policy = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": ["s3:GetObject"],
                        "Resource": [f"arn:aws:s3:::{MINIO_BUCKET}/*"]
                    }
                ]
            }
            import json
            s3_client.put_bucket_policy(Bucket=MINIO_BUCKET, Policy=json.dumps(policy))
        except Exception as e:
            print(f"Error creating bucket: {e}")

async def upload_file_to_minio(file: UploadFile, filename: str) -> str:
    ensure_bucket_exists()
    try:
        s3_client.upload_fileobj(
            file.file,
            MINIO_BUCKET,
            filename,
            ExtraArgs={"ContentType": file.content_type}
        )
        return f"{MINIO_ENDPOINT}/{MINIO_BUCKET}/{filename}"
    except Exception as e:
        print(f"Failed to upload: {e}")
        return None
