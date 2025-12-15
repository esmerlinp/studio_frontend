import streamlit as st
from app.utils import i18n
from app.services.auth_service import login

def login_form(cookies):
    with st.form("login_form", enter_to_submit=True, clear_on_submit=False, border=True):
        username = st.text_input(f"{i18n._('login.username')}")
        password = st.text_input(f"{i18n._('login.password')}", type="password")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            data_auth = login(user_name=username, password=password)
            if data_auth:
                cookies["is_auth"] = str(True)
                cookies["accessToken"] = data_auth.accessToken
                cookies["refreshToken"] = data_auth.refresh_token
                cookies["me"] = str(data_auth.__dict__)
                cookies.save()
                st.rerun()
            else:
                st.warning(f"{i18n._('login.error_empty_fields')}")
                st.stop()
            