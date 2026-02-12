from fastapi import FastAPI
from app.controllers.user_controller import router
from app.core.database import engine
from app.core.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API CRUD con FastAPI")

app.include_router(router)
