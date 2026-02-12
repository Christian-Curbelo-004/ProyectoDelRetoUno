from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.user import UserCreate, UserResponse
from app.service import user_service


router = APIRouter(prefix="/users", tags=["users"])

def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@router.post("/",c) 

 # data (nombre del parametro que recibira los datos del usuario): UserCreate (define los campos de JSON, esto es de pydantic) >>> db: nombre del parametro que tendra la sesion de db
 # Session indica que sera una db
 # Depends(get_db)):  inyeccion de dependencias de fastapi, cuando llamen al endpoint, ejecuta get_db() para obtener la sesion de db y se la pasa a la funcion create_user_endpoint
def create_user_endpoint(data: UserCreate, db: Session = Depends(get_db)): 
    return user_service.create_user(db, data)                               




@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return user_service.list_users(db)
