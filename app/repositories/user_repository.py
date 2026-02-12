from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository: # interactua con la bd
    def create(self, db: Session, user : User):
        db.add(user) # agrega al usuario
        db.commit() # confirma la transaccion, guarda los cambios en la base de datos
        db.refresh(user) # refresca el objeto user para obtener los datos actualizados de la base de datos, como el id generado automáticamente
        return user
    

    def get_all(self, db: Session): # muestra todos los usuarios
        return db.query(User).all()
    
    def get_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first() # filtra por id y devuelve el primer resultado encontrado