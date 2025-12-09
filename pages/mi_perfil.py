import streamlit as st
from util import i18n
from core import fetch_data
from streamlit_avatar import avatar

# st.set_page_config(
#     layout="wide"
# )

#if not 'user' in st.session_state or not st.session_state.user:
with st.spinner():
    #data = fetch_data("api/users/2")
    data = fetch_data("me")
   
    st.write(data)
    st.stop()
        
    st.session_state.user = data["result"]


with st.sidebar:
    st.button("Cerrar sesión", width="stretch")


st.write("**My account**")
key = "main_cont"
# Estilos solo para el contenedor con esta key


st.markdown(
    f"""
    <style>
        /* Selector para el container con la key específica */
        .st-key-{key} {{
            background-color: #f0f0f0 !important;  /* Cambia aquí el color de fondo */
            border-radius: 1rem; /* Ejemplo de estilo adicional */
            padding: -1rem;       /* Ejemplo de padding para que el cambio se note */
            margin-top: -1rem;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
        

with st.container(border=True, key=key):
    # if st.button("__Theme__", type="tertiary", help=":gray[That's theme pretty]"):
    #     st.switch_page("pages/learn.py")
    if st.session_state.user:
        me = st.session_state.user
        imagen = me.get('photo', None)  
        if not imagen:
            imagen = "https://picsum.photos/id/237/300/300"
            
        avatar(
            [
                {
                    "url": imagen,
                    "size": 60,
                    "title": me['firstName'],
                    "caption": me['email'],
                    "key": "avatar1",
                },
            ]
        )

        st.write("---")
        if st.button("__Cerrar Sesión__", help=":gray[That's theme pretty]", type="primary"):
            st.switch_page("pages/learn.py")
        # if st.button(i18n._("app.footer"), help=":gray[That's theme pretty]", type="secondary"):
        #     st.switch_page("pages/learn.py")
        
        st.write(me)
