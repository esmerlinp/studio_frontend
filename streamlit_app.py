import streamlit as st
from util import i18n
# Configuración de la página
st.set_page_config(
    page_title="stdio",
    page_icon="🚀",
    layout="centered"
)

# ------------------------------
# Configuración de idioma
# ------------------------------
culture = "es-DO"
#culture = st.context.locale
query_params = st.query_params
st.session_state.idioma = culture.split("-")[0] 
i18n.setup_gettext(st.session_state.idioma)


pages = {
    "Your account": [
        st.Page("pages/home.py", title="Home"),
        st.Page("pages/create_account.py", title="Create your account"),
        st.Page("pages/manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("pages/learn.py", title="Learn about us"),
        st.Page("pages/trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()