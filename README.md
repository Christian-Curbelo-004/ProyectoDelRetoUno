🚀 Proyecto del Reto Uno
📌 Descripción

Este proyecto consiste en levantar un agente utilizando FastAPI como framework principal.

Actualmente la aplicación se ejecuta en entorno local, permitiendo visualizar y probar los endpoints mediante la documentación automática que provee FastAPI.

🛠 Tecnologías utilizadas

Python 3.13

FastAPI

Uvicorn

Pydantic

SQLAlchemy

▶️ Cómo ejecutar el proyecto

Clonar el repositorio

git clone <url-del-repo>
cd ProyectoDelRepoUno


Crear y activar entorno virtual

python -m venv venv
venv\Scripts\activate   # En Windows


Instalar dependencias

pip install -r requirements.txt


Levantar el servidor

python -m uvicorn app.main:app --reload

🌐 Acceso local

El proyecto corre en:

http://127.0.0.1:8000


La documentación interactiva (Swagger) está disponible en: local host port: /docs


Desde allí se pueden probar los endpoints del agente directamente.

📂 Estado actual

✔ Proyecto funcionando en entorno local
✔ Documentación automática habilitada
✔ Estructura organizada tipo MVC

🎯 Objetivo

Desarrollar progresivamente un agente backend estructurado, escalable y organizado, siguiendo buenas prácticas de arquitectura.
