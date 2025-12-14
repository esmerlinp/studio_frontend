import streamlit as st
from app.utils import i18n
from streamlit_avatar import avatar
from app.services.user_service import get_user

# st.set_page_config(
#     layout="wide"
# )

# if not 'user' in st.session_state or not st.session_state.user:
#     with st.spinner():
#         #data = user_service.get_user_by_id(st.session_state.user['userId'])
#         user = get_user(user_id=2)
        
#         st.session_state.user = user


with st.sidebar:
    st.button("Cerrar sesión", width="stretch")


st.header("Manage Account")
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
            margin-bottom: -3rem;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
        

with st.container(border=True, key=key):
    # if st.button("__Theme__", type="tertiary", help=":gray[That's theme pretty]"):
    #     st.switch_page("pages/learn.py")
    if st.session_state.me:
        me = st.session_state.me
        imagen = me.photo
        fullname = f"{me.firstName} {me.lastName}"
        if not imagen:
            imagen = f"https://ui-avatars.com/api/?background=27414fff&color=ffffff&name={fullname}=100%bold=true"
            
        avatar(
            [
                {
                    "url": imagen,
                    "size": 60,
                    "title": fullname,
                    "caption": me.email,
                    "key": "avatar1",
                },
            ]
        )

with st.container():
    if st.session_state.me:
        me = st.session_state.me
  

        
        st.divider()
        st.text_input("Name", me.firstName, disabled=False)
        st.caption("Your name may appear around GitHub where you contribute or are mentioned. You can remove it at any time.")
        
        st.text_input("Email", me.email, disabled=False)
        st.caption("Your name may appear around GitHub where you contribute or are mentioned. You can remove it at any time.")
        
        st.text_area("Bio", "Coordinador de Desarrollo de Software", disabled=False, height=200)
        st.caption("Your name may appear around GitHub where you contribute or are mentioned. You can remove it at any time.")

            
# with st.container():

    
#     sesiones_activas  = fetch_data(f"api/v1/auth/sessions")
#     result = sesiones_activas.get("result", [])
#     for i, s in enumerate(result):
        
#         with st.container(border=True, horizontal=True):
#             #st.image(":material/rule_settings:")
#             if st.button(label="", type="tertiary", key=f"session_icon_{i}", icon=":material/public_off:"):
#                 with st.spinner("Closing session..."):
#                     result = api_user.close_sesion(s["sessionId"])
#                     st.write(result)
#                     # if "error" in result:
#                     #     st.error(result["error"])
#                     # else:
#                     #     st.rerun()
                
#             with st.container(horizontal=True):
#                 st.markdown(f'__{s["device"]}__')
#                 st.caption(f'Última actividad: {s["lastAccess"]}  expired on {s["expired"]} from IP: {s["deviceIp"]}')
#             #st.badge("current", color="green")
#             st.space("stretch")
#             st.button("__Cerrar__",  type="tertiary", key=f"close_session_{i}")

    # if st.button("__Theme__", type="tertiary", help=":gray[That's theme pretty]"):
    #     me  = fetch_data(f"api/me")
