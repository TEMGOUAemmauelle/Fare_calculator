from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, auth, crud

router = APIRouter(prefix="/fares", tags=["fares"])

@router.post("/calculate", response_model=schemas.FareEstimateResponse)
def calculate_fare(request: schemas.FareCalculateRequest):
    if not request.startLocationName or not request.endLocationName:
        raise HTTPException(status_code=400, detail="Start and end location names must be provided.")
    # Logique mock (à remplacer plus tard par calcul réel)
    return schemas.FareEstimateResponse(
        estimatedFare=350,
        officialFare=300,
        distanceInKm=2.8,
        startLocationName=request.startLocationName,
        endLocationName=request.endLocationName
    )

@router.post("/submit-actual", status_code=201)
def submit_actual(request: schemas.SubmitActualRequest, user_id: str = Depends(auth.get_current_user), db: Session = Depends(database.get_db)):
    # Ici on pourrait enregistrer dans submitted_fares si besoin
    return {"message": "Fare data recorded successfully."}
