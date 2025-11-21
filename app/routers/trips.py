from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from app.models import Trip
from app.schemas import TripCreate, TripUpdate, TripOut

router = APIRouter(prefix="/trips",tags=["Trips"])

@router.post("/",response_model=TripOut)
def create_trip(trip: TripCreate, db: Session = Depends(get_db)):
    db_trip = Trip(**trip.model_dump())
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

@router.get("/", response_model=List[TripOut])
def list_trips(db: Session = Depends(get_db)):
    return db.query(Trip).all()

@router.get("/{trip_id}", response_model=TripOut)
def get_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip

@router.patch("/{trip_id}",response_model=TripOut)
def update_trip(trip_id: int, trip_update: TripUpdate, db: Session = Depends(get_db)):
    db_trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not db_trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    #Update only provided fields
    update_data = trip_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_trip, key, value)

    db.commit()
    db.refresh(db_trip)
    return db_trip