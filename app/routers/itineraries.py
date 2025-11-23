from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, auth, database

router = APIRouter(prefix="/itineraries", tags=["itineraries"])

@router.get("/me", response_model=List[schemas.ItineraryResponse])
def get_my_itineraries(user_id: str = Depends(auth.get_current_user), db: Session = Depends(database.get_db)):
    return crud.get_user_itineraries(db, user_id)

@router.post("/me")
def update_my_itineraries(request: schemas.ItinerariesUpdate, user_id: str = Depends(auth.get_current_user), db: Session = Depends(database.get_db)):
    crud.upsert_user_itineraries(db, request.itineraries, user_id)
    return {"message": "Itineraries updated successfully."}
