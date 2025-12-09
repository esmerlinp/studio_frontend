import streamlit as st
from util import i18n
from core import login


def login_page(cookies):
    st.title("Inicio de Sesión")
    st.write("Simulación de login…")
    

    user = st.text_input(f"{i18n._('login.username')}")
    password = st.text_input(f"{i18n._('login.password')}", type="password")

    

    if st.button("Entrar"):
        # Simulación
        result = login(user_name=user, password=password)
        if result:
            cookies["is_auth"] = str(True)
            cookies["accessToken"] = result['accessToken']
            cookies["refreshToken"] = result['refresh_token']
            cookies.save()
            st.rerun()
        else:
            #st.warning()
            st.warning(f"{i18n._('login.error_empty_fields')}")
            st.stop()
        # st.write(result)
        # # if result['mensaje']:
        # #     st.session_state.logged = True
        # #     st.rerun()
        # # else:
        # #     st.error(f"{i18n._('login.error_empty_fields')}")
