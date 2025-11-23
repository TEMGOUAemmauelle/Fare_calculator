from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from .database import Base

class Itinerary(Base):
    __tablename__ = "itineraries"
    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    start_location_name = Column(String, index=True)
    end_location_name = Column(String, index=True)
    saved_fare = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SubmittedFare(Base):
    __tablename__ = "submitted_fares"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    start_location_name = Column(String)
    end_location_name = Column(String)
    actual_fare = Column(Integer)
    completed_at = Column(DateTime(timezone=True))
