from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class FareCalculateRequest(BaseModel):
    startLocationName: str
    endLocationName: str
    departureTime: str

class FareEstimateResponse(BaseModel):
    estimatedFare: int
    officialFare: int
    distanceInKm: float
    startLocationName: str
    endLocationName: str

class SubmitActualRequest(BaseModel):
    startLocationName: str
    endLocationName: str
    actualFare: int
    completedAt: datetime

class ItineraryBase(BaseModel):
    startLocationName: str
    endLocationName: str
    savedFare: int

class ItineraryCreate(ItineraryBase):
    pass

class ItineraryResponse(ItineraryBase):
    id: str

class ItinerariesUpdate(BaseModel):
    itineraries: List[ItineraryCreate]
