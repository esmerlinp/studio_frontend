import streamlit as st
from core import fetch_data

def get_user_by_id(user_id: int) -> dict:
    
    data = fetch_data(f"api/users/{user_id}")
    return data

def close_sesion(sessionId: int) -> dict:
    
    data = fetch_data(f"api/sessions/close/{sessionId}", method="PUT")
    return data