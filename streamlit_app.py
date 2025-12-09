import streamlit as st
from util import i18n
from pages.modulos import academico, cafeteria, padres, enfermeria, financiero
from pages import login_page, modules_page

from st_cookies_manager import EncryptedCookieManager
import os

# -------------------------------------------------------
# Configuración de la app
# -------------------------------------------------------
st.set_page_config(
    page_title="stdio",
    page_icon="🚀",
    layout="centered"
)

custom_styles = """ 
    <style>
        .block-container {
            padding-top: 0rem;
        }
        div.block-container {
            padding-top: 1rem; /* Ajusta aquí el margen superior */
        }
    </style>
"""
st.markdown(custom_styles, unsafe_allow_html=True)

# ------------------------------
# Configuración de idioma
# ------------------------------
culture = "es-DO"
st.session_state.idioma = culture.split("-")[0]
i18n.setup_gettext(st.session_state.idioma)


# ------------------------------
# Inicializar cookies
# ------------------------------
cookies = EncryptedCookieManager(
    prefix=f"camsoft/self-services_AKADMIA",
    password=os.environ.get("COOKIES_PASSWORD", "sdius-8uyyhh-tthhn87"),
)

if not cookies.ready():
    st.stop()
    

if not 'update_token' in st.session_state:
    st.session_state.update_token = False

if st.session_state.update_token == True:
    cookies['accessToken'] = st.session_state.refreshToken
    st.session_state.update_token = False
    
    
# ------------------------------
# Estado de autenticación
# ------------------------------
st.session_state.is_auth = cookies.get("is_auth", False)
st.session_state.accessToken = cookies.get("accessToken", "")
st.session_state.refreshToken = cookies.get("refreshToken", "")


# -------------------------------------------------------
# LÓGICA PRINCIPAL
# -------------------------------------------------------

# Inicializar variables de sesión
# if "logged" not in st.session_state:
#     st.session_state.logged = False

if "modulo_actual" not in st.session_state:
    st.session_state.modulo_actual = None

# Si no está logueado → mostrar login
if not st.session_state.is_auth:
    login_page.login_page(cookies=cookies)
    
elif st.session_state.modulo_actual is None:
    modules_page.modules_page()

# Si ya eligió un módulo → cargar su navegación
else:
    #st.title(f"Módulo: {st.session_state.modulo_actual}")

    # Definir listas de páginas según el módulo elegido
    if st.session_state.modulo_actual == f"{i18n._("module.academico")}":
        pages = academico.academic_pages()

    elif st.session_state.modulo_actual == f"{i18n._("module.cafeteria")}":
        pages = cafeteria.get_pages()

    elif st.session_state.modulo_actual == f"{i18n._("module.enfermeria")}":
        pages = enfermeria.get_pages()

    elif st.session_state.modulo_actual == f"{i18n._("module.financiero")}":
        pages = financiero.get_pages()

    elif st.session_state.modulo_actual == f"{i18n._("module.padres")}":
        pages = padres.get_pages()

    else:
        st.error(f"{i18n._('error.module_unknown')}")
        st.stop()

    # Usar navegación
 
    pg = st.navigation(pages)
    pg.run()
