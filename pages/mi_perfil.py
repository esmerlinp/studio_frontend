import streamlit as st
from util import i18n
from core import user_service
from streamlit_avatar import avatar

# st.set_page_config(
#     layout="wide"
# )

#if not 'user' in st.session_state or not st.session_state.user:
# with st.spinner():
#     data = user_service.get_user_by_id(st.session_state.user['userId'])
#     error = data.get("error", None)
#     if error:
#         if error['msg']:
#             st.error(error['msg'])
#         if error['error']:
#             st.error(error['error'])
#         st.stop()
#     #data = fetch_data("me")
   
#     st.write(data)
#     st.stop()
        
#     st.session_state.user = data["result"]


with st.sidebar:
    st.button("Cerrar sesión", width="stretch")


st.header("**My account**")
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
        fullname = f"{me['firstName']} {me['lastName']}"
        if not imagen:
            imagen = f"https://ui-avatars.com/api/?background=27414fff&color=ffffff&name={fullname}=100%bold=true"
            
        avatar(
            [
                {
                    "url": imagen,
                    "size": 60,
                    "title": fullname,
                    "caption": me['email'],
                    "key": "avatar1",
                },
            ]
        )
with st.container(border=True,):
    # if st.button("__Theme__", type="tertiary", help=":gray[That's theme pretty]"):
    #     st.switch_page("pages/learn.py")
    if st.session_state.user:
        if st.button("__Cerrar Sesión__", help=":gray[That's theme pretty]", type="primary"):
            print("cerrar cession")
        # if st.button(i18n._("app.footer"), help=":gray[That's theme pretty]", type="secondary"):
        #     st.switch_page("pages/learn.py")
        
        #st.write(me)
