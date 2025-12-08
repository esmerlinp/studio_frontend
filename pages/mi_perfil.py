import streamlit as st
from util import i18n

# st.set_page_config(
#     layout="wide"
# )

with st.sidebar:
    st.button("Cerrar sesión", width="stretch")


st.write("**Appearance**")
key = "main_cont"
# Estilos solo para el contenedor con esta key
st.markdown(
    f"""
    <style>
        /* Selector para botones dentro del container con key específica */
        .st-key-{key} div[data-testid="stButton"]>button {{
            min-height: 10px;    /* altura mínima */
            height: 10px;        /* altura exacta */
            margin-top: 0px;     /* margen superior */
            margin-bottom: 0px;  /* margen inferior */
            margin-left: 10px;   /* margen izquierdo */
            padding-top: 4px;    /* padding interno */
            padding-bottom: 4px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
        

with st.container(border=True, key=key):
    # if st.button("__Theme__", type="tertiary", help=":gray[That's theme pretty]"):
    #     st.switch_page("pages/learn.py")
    st.write("---")
    st.caption("Caption button")    
    if st.button("__Theme__", help=":gray[That's theme pretty]", type="primary"):
        st.switch_page("pages/learn.py")
    if st.button(i18n._("app.footer"), help=":gray[That's theme pretty]", type="secondary"):
        st.switch_page("pages/learn.py")
    
