# services/s3_service.py

import boto3
import uuid
import os

s3 = boto3.client("s3")
BUCKET_NAME = "your-bucket-name"

def upload_to_s3(file_obj, filename=None):
    if not filename:
        filename = str(uuid.uuid4()) + "-" + file_obj.filename

    s3.upload_fileobj(
        Fileobj=file_obj,
        Bucket=BUCKET_NAME,
        Key=filename,
        ExtraArgs={"ACL": "private"}
    )
    return filename, f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"

def download_from_s3(filename, local_path):
    s3.download_file(BUCKET_NAME, filename, local_path)

def delete_from_s3(filename):
    s3.delete_object(Bucket=BUCKET_NAME, Key=filename)
