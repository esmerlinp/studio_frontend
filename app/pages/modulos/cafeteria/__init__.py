import streamlit as st
from app.utils import i18n





def get_pages():
    pages = {
        f"{i18n._('menu.admisiones')}": [
            st.Page("app/pages/modulos/academico/admiciones/solicitud_admision.py", title=f"{i18n._('menu.solicitud_admision')}"),
            st.Page("app/pages/modulos/academico/admiciones/evaluacion_admisiones.py", title=f"{i18n._('menu.evaluacion_admisiones')}"),
            st.Page("app/pages/modulos/academico/admiciones/inscripcion_estudiantes.py", title=f"{i18n._('menu.inscripcion_estudiantes')}"),
        ]}
    return pages
    