from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime
from app.db import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer,ForeignKey("trips.id"))
    type = Column(String)
    file_url = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

    #Back reference to Trip
    trip = relationship("Trip", back_populates="documents")