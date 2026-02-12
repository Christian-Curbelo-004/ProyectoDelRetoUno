from fastapi import FastAPI # importamos FastAPI para crear la aplicación principal
from app.controller.user_controller import router #importamos el router de user_controller para incluirlo en la aplicación principal
from app.core.database import engine # motor de base de datos
from app.core.database import Base

Base.metadata.create_all(bind=engine) # creamos tablas de db

app = FastAPI(title="API FASTAPI") # titulo

app.include_router(router) # 


# uvicorn app.main:app --reload >>>>> el reload sirve para que se actualice el servidor cada vez que se hacen cambios
# ejecutamos el comando de arriba para iniciar el servidor de desarrollo y poder probar la API en http://localhost:8000/docs
# lo ejecutamos en la rais del proyecto