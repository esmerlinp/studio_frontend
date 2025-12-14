from app.api.api_user import get_user_by_id
from app.models.user_model import UserModel


def get_user(user_id: int) -> UserModel | None:
    return get_user_by_id(user_id=user_id)
