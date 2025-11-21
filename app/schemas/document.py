from datetime import datetime
from .base import AppBaseModel

class DocumentBase(AppBaseModel):
    type: str

class DocumentOut(DocumentBase):
    id: int
    trip_id: int
    file_url: str
    created_at: datetime