# app/service/user_service.py

def create_user(user_data):
    # TODO: Add database logic to create user
    return {
        "name": user_data.name,
        "email": user_data.email
    }

def list_users():
    # TODO: Add database logic to list users
    return []
