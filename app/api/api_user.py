
from app.api import api_request
from app.models.user_model import UserModel
from typing import Optional

def get_user_by_id(user_id: int) -> Optional[UserModel]:
    response = api_request(f"/users/{user_id}")
    
    if not response or response.get("success") is not True:
        return None
    
    data = response.get("data")
    if not data:
        return None

    return UserModel(**data)


def get_user_by_id(user_id: int) -> dict:
    data = api_request(f"/users/{user_id}")
    return data

def close_sesion(sessionId: int) -> dict:
    
    data = api_request(f"/auth/sessions/close/{sessionId}", method="PUT")
    return data