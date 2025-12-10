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
    
if not 'user' in st.session_state:
    st.session_state.user = None
    

  
if not 'update_token' in st.session_state:
    st.session_state.update_token = False

if not 'force_login' in st.session_state:
    st.session_state.force_login = False
    
if "modulo_actual" not in st.session_state:
    st.session_state.modulo_actual = None
    
if st.session_state.force_login == True:
    @st.dialog("Session Expired", width="small", dismissible=False)
    def inactivity_modal():
        st.title("Sesión Expirada por Inactividad")
        st.caption(
            "Por motivos de seguridad, tu sesión ha sido cerrada automáticamente "
            "debido a un período prolongado sin actividad."
        )
        
        st.markdown(
            """
            Para continuar utilizando la plataforma, inicia sesión nuevamente.  
            Esto garantiza la protección de tu información y el correcto funcionamiento del sistema.
            """
        )

        if st.button("Ir a la pantalla de inicio de sesión", type="primary"):
            cookies["is_auth"] = str(False)
            cookies["accessToken"] = ""
            cookies["refreshToken"] = ""

            # Limpiar variables de sesión
            del st.session_state.is_auth
            del st.session_state.user
            del st.session_state.accessToken
            del st.session_state.refreshToken
            del st.session_state.force_login
            del st.session_state.modulo_actual
            
            st.rerun()

    inactivity_modal()
    st.stop()
    

#st.write(cookies)
if st.session_state.update_token == True:
    cookies['accessToken'] = st.session_state.refreshToken
    st.session_state.update_token = False
    
    
# ------------------------------
# Estado de autenticación
# ------------------------------
raw_value = cookies.get("is_auth", "false")
st.session_state.is_auth = str(raw_value).lower() == "true" 
st.session_state.accessToken = cookies.get("accessToken", "")
st.session_state.refreshToken = cookies.get("refreshToken", "")


# -------------------------------------------------------
# LÓGICA PRINCIPAL
# -------------------------------------------------------


st.write(st.session_state.is_auth)
st.write(f"force login: {st.session_state.force_login}")


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
