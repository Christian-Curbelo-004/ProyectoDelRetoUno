from sqlalchemy import create_engine # creamos un motor de base de datos utilizando SQLAlchemy, esto nos sirve en las DBAPI
from sqlalchemy.orm import sessionmaker, declarative_base # sesssionmaker nos permite crear sesiones para interactura con la db

database_url = "sqlite:///./test.db"

engine = create_engine(database_url, connect_args={"check_same_thread": False}) # creamos el motor de base de datos utilizando la URL de la base de datos y configuramos la conexión para SQLite

Sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine) # creamos una clase de sesión utilizando sessionmaker, configuramos autocommit y autoflush en False y vinculamos el motor de base de datos

class Base: # creamos una clase base para nuestros modelos de base de datos utilizando declarative_base, esto nos permite definir nuestras tablas como clases de Python
    pass 

