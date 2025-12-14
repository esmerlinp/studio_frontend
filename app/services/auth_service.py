from app.api.api_auth import authenticate
from app.models.auth_model import AuthenticationModel
import streamlit as st



from typing import Optional


def login(user_name: str, password: str) -> Optional[AuthenticationModel]:

    credentials = {
        "username": user_name,
        "password": password
    }

    auth = authenticate(credentials=credentials)
    if not auth:
        return None
    
    # Manejo de sesión
    st.session_state.accessToken = auth.accessToken
    st.session_state.refreshToken = auth.refresh_token
    st.session_state.me = auth

    return auth


def log_out():
    
    return True