# Modelo ORM (Object-Relational Mapping) para la tabla de usuarios en la base de datos

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class User(Base):
    _tablename_ = "users" # creamos la tabla de usuarios en la base de datos, el nombre de la tabla es "users"
     
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True) # relacionamos  el campo id con la columna id de la tabla, el tipo de dato es Integer, es la clave primaria y se indexa para mejorar el rendimiento de las consultas
    name: Mapped[str] = mapped_column(String, nullable=False) # relacionamos el campo name con la columna name de la tabla, el tipo de dato es String y no puede ser nulo
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)  # relacionamos el campo email con la columna email de la tabla, el tipo de dato es String, debe ser único, se indexa para mejorar el rendimiento de las consultas y no puede ser nulo
    