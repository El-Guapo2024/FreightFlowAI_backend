import shutil
import os
from fastapi import UploadFile
import time

ALLOWED_TYPES = ["application/pdf","image/png","image/jpeg"]

UPLOAD_DIR = "local_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def run_ocr(file_path: str, document_type: str = "BOL"):
    """
    Simulates OCR Processing
    """
    print(f"Running OCR on {file_path}...")
    time.sleep(2)

    if document_type == "RATE_CONFIRMATION":
        return {
            "status": "completed",
            "extracted_text": f"OCR results for {file_path}",
            "confidence": 0.98,
            "processing_time": 2,
            "data": {
                "pickup_city": "New York",
                "dropoff_city": "Los Angeles",
                "broker_id": "CHROBINSON",
                "rate": 100.00
            }
        }

    return {
        "status": "completed",
        "extracted_text": f"OCR results for {file_path}",
        "confidence": 0.98,
        "processing_time": 2,
        "data": {
            "invoice_number": "INV-1001",
            "amount": 500.00
        }
    }

def upload_document(file: UploadFile) -> str:
    """
    Saves an uploaded file to the local filesystem.
    Returns the file path (URL).
    """
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type")
    # Create a safe file path
    # Use file.filename to get the actual name of the uploaded file
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    
    # Write the file bytes to disk
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return file_location
