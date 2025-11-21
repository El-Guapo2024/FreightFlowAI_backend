from datetime import datetime
from typing import List, Optional
from .base import AppBaseModel
from .document import DocumentOut

class TripBase(AppBaseModel):
    pickup_city: str
    dropoff_city: str
    broker_id: Optional[str] = None
    driver_id: Optional[int] = None

class TripCreate(TripBase):
    pass

class TripUpdate(AppBaseModel):

    pickup_city: Optional[str] = None
    dropoff_city: Optional[str] = None
    status: Optional[str] = None

class TripOut(TripBase):
    id: int
    status: str
    created_at: datetime
    # Nested model: this will return the list of documents inside the trip object

    documents: List[DocumentOut] = []

    