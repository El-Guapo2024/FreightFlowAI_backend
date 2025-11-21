import shutil
import os
from fastapi import UploadFile

UPLOAD_DIR = "local_files"
os.makedirs(UPLOAD_DIR, exist_ok = True)

def run_ocr(file_path: str):
    """
    Placeholder for future OCR logic.
    For now, it just prints a message.
    """

    print(f"Running OCR on {file_path}...")
    return {"status":"pending", "text":"OCR not implemented yet"}

def upload_document(file: UploadFile) -> str:
    """
    Saves an uploaded file to the local filesystem.
    Returns the file path (URL).
    """

    # Create a safe file path
    file_location = f"{UPLOAD_DIR}/{file.name}"

    # Write the file bites to disk
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return file_location