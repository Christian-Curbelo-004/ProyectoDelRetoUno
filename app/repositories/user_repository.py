from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository: # interactua con la bd
    def create(self, db: Session, user : User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    

    def get_all(self, db: Session): # muestra todos los usuarios
        return db.query(User).all()
    
    def get_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first() # filtra por id y devuelve el primer resultado encontrado