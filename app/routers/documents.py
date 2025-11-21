from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from app.models import Document, Trip
from app.schemas import DocumentOut
from app.services import upload_document, run_ocr

router = APIRouter(prefix="/trips",tags=["Documents"])

@router.post("/{trip_id}/documents",response_model=DocumentOut)
def upload_trip_document(
    trip_id: int,
    type: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Check if trip exists
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    # Upload file using Service
    file_url = upload_document(file)

    # Create DB record
    db_document = Document(
        trip_id = trip_id,
        type=type,
        file_url=file_url
    )

    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    # Trigger OCR (async in future)
    run_ocr(file_url)

    return db_document

@router.get("/{trip_id}/documents", response_model=List[DocumentOut])
def list_trip_documents(trip_id: int, db: Session = Depends(get_db)):

    return db.query(Document).filter(Document.trip_id == trip_id).all()