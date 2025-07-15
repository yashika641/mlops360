# routes/upload_route.py

from fastapi import APIRouter, UploadFile, File
from services.s3_service import upload_to_s3, download_from_s3, delete_from_s3
import os

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    filename, s3_url = upload_to_s3(file.file, file.filename)

    # Simulate processing (optional)
    local_path = f"temp/{filename}"
    os.makedirs("temp", exist_ok=True)
    download_from_s3(filename, local_path)

    # Your custom logic (mocked here)
    result = f"Processed {filename}"

    # Remove after use
    delete_from_s3(filename)

    return {
        "file_url": s3_url,
        "message": result
    }
