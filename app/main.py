from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from datetime import datetime
from .database import engine, Base
from .routers import fares, itineraries
from . import auth

# Création des tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fare Calculator API - TraEnSys",
    description="API conforme à la spécification v1.0",
    version="1.0",
    docs_url="/docs"
)

app.include_router(fares.router, prefix="/api/v1")
app.include_router(itineraries.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Fare Calculator API is running!"}

# Endpoint pour générer un token de test (à supprimer en prod)
@app.post("/dev/token")
def dev_token():
    token = auth.create_access_token({"sub": "test_user_123"})
    return {"access_token": token, "token_type": "bearer"}

# Gestion d'erreurs conforme à la spec
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    status_code = 500
    if isinstance(exc, HTTPException):
        status_code = exc.status_code
    return JSONResponse(
        status_code=status_code,
        content={
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "status": status_code,
            "error": "Internal Server Error" if status_code >= 500 else "Bad Request",
            "message": str(exc) if status_code < 500 else "Internal server error",
            "path": str(request.url)
        }
    )
