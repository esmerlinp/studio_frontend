from app.api import api_request
from typing import Optional
from app.models.auth_model import AuthenticationModel

def authenticate(credentials: dict) -> Optional[AuthenticationModel]:
    response = api_request(
        endpoint="/auth/login",
        method="POST",
        body_params=credentials
    )

    if not response or response.get("success") is not True:
        return None

    data = response.get("data")
    if not data:
        return None

    return AuthenticationModel(**data)
    