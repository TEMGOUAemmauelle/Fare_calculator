from sqlalchemy.orm import Session
from . import models, schemas
import uuid

def get_user_itineraries(db: Session, user_id: str):
    return db.query(models.Itinerary).filter(models.Itinerary.user_id == user_id).all()

def upsert_user_itineraries(db: Session, itineraries: list[schemas.ItineraryCreate], user_id: str):
    # Supprime les anciens
    db.query(models.Itinerary).filter(models.Itinerary.user_id == user_id).delete()
    # Ajoute les nouveaux
    for item in itineraries:
        db_item = models.Itinerary(
            id=f"iti_{uuid.uuid4().hex[:12]}",
            user_id=user_id,
            start_location_name=item.startLocationName,
            end_location_name=item.endLocationName,
            saved_fare=item.savedFare
        )
        db.add(db_item)
    db.commit()
