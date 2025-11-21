from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.db import Base

class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True,index=True)
    driver_id = Column(Integer, nullable=True)
    broker_id = Column(String, nullable=True) 
    pickup_city = Column(String, nullable=True)
    dropoff_city = Column(String, nullable=True)
    status = Column(String, default="planned")
    rate = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

    # Relationship to documents
    # "Document" is the class name, "trip" is the back_populates attribute in Document
    documents = relationship("Document", back_populates="trip")