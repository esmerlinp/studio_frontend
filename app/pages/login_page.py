import streamlit as st
from app.utils import i18n
from app.forms.login_form import login_form


def login_page(cookies):
    st.title("Inicio de Sesión")
    login_form(cookies)
