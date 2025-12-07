import streamlit as st
from util import i18n
from pages.modulos.academico import academic_pages  # Tu módulo existente
from pages.modulos import academico, cafeteria, padres, enfermeria, financiero
# -------------------------------------------------------
# Configuración de la app
# -------------------------------------------------------
st.set_page_config(
    page_title="stdio",
    page_icon="🚀",
    layout="centered"
)

# ------------------------------
# Configuración de idioma
# ------------------------------
culture = "es-DO"
st.session_state.idioma = culture.split("-")[0]
i18n.setup_gettext(st.session_state.idioma)

# -------------------------------------------------------
# FUNCIONES SIMULADAS — luego las reemplazas
# -------------------------------------------------------

def login_page():
    st.title("Inicio de Sesión")
    st.write("Simulación de login…")

    user = st.text_input(f"{i18n._('login.username')}")
    password = st.text_input(f"{i18n._('login.password')}", type="password")

    if st.button("Entrar"):
        # Simulación
        if user and password:
            st.session_state.logged = True
            st.rerun()
        else:
            st.error(f"{i18n._('login.error_empty_fields')}")



icons = {
    f"{i18n._("module.academico")}": "📚",
    f"{i18n._("module.cafeteria")}": "🍽️",
    f"{i18n._("module.enfermeria")}": "🩺",
    f"{i18n._("module.financiero")}": "💰",
    f"{i18n._("module.padres")}": "👨‍👩‍👧",
}

modulos = {
    i18n._("module.academico"): i18n._("module.academico.description"),
    i18n._("module.cafeteria"): i18n._("module.cafeteria.description"),
    i18n._("module.enfermeria"): i18n._("module.enfermeria.description"),
    i18n._("module.financiero"): i18n._("module.financiero.description"),
    i18n._("module.padres"): i18n._("module.padres.description"),
}


def modules_page():
    st.title(f"{i18n._('modules.select_title')}")
    st.write(f"{i18n._('modules.select_subtitle')}")

    # Dividir las tarjetas en columnas de forma dinámica
    cols = st.columns(2)

    for index, (modulo, descripcion) in enumerate(modulos.items()):
        col = cols[index % 2]

        with col:
            st.markdown(
                f"""
                <div style="
                    padding: 15px;
                    border-radius: 12px;
                    border: 1px solid #E5E5E5;
                    margin-bottom: 20px;
                    text-align: center;
                    background-color: #FAFAFA;">
                    <div style="font-size: 40px;">{icons.get(modulo, '📦')}</div>
                    <h4 style="margin-top: 10px;">{modulo}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.caption(descripcion)

            if st.button(f"{i18n._('modules.access_button')} {modulo}", key=f"btn_{modulo}"):
                st.session_state.modulo_actual = modulo
                st.rerun()


# ------------------------------
# Páginas simuladas por módulo
# ------------------------------






# -------------------------------------------------------
# LÓGICA PRINCIPAL
# -------------------------------------------------------

# Inicializar variables de sesión
if "logged" not in st.session_state:
    st.session_state.logged = False

if "modulo_actual" not in st.session_state:
    st.session_state.modulo_actual = None

# Si no está logueado → mostrar login
if not st.session_state.logged:
    login_page()

# Si está logueado y no ha elegido módulo aún
elif st.session_state.modulo_actual is None:
    modules_page()

# Si ya eligió un módulo → cargar su navegación
else:
    st.title(f"Módulo: {st.session_state.modulo_actual}")

    # Definir listas de páginas según el módulo elegido
    if st.session_state.modulo_actual == f"{i18n._("module.academico")}":
        pages = academic_pages()

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
