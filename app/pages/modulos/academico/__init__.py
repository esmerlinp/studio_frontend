import streamlit as st
from app.utils import i18n


def academic_pages():
    pages = {
        f"{i18n._("menu.admisiones")}": [
            st.Page("app/pages/modulos/academico/admiciones/solicitud_admision.py", title=f"{i18n._("menu.solicitud_admision")}", icon=":material/how_to_reg:"),
            st.Page("app/pages/modulos/academico/admiciones/evaluacion_admisiones.py", title=f"{i18n._("menu.evaluacion_admisiones")}", icon=":material/edit_calendar:"),
            st.Page("app/pages/modulos/academico/admiciones/inscripcion_estudiantes.py", title=f"{i18n._("menu.inscripcion_estudiantes")}", icon=":material/person_add:"),
        ],
        f"{i18n._("menu.estudiantes")}": [
            st.Page("app/pages/modulos/academico/estudiantes/expedientes.py", title=f"{i18n._("menu.expedientes")}", icon=":material/developer_guide:"),
            st.Page("app/pages/modulos/academico/estudiantes/asistencias.py", title=f"{i18n._("menu.asistencias")}", icon=":material/playlist_add_check:"),
            st.Page("app/pages/modulos/academico/estudiantes/correccion_notas.py", title=f"{i18n._("menu.correccion_notas")}", icon=":material/done_all:"),
            st.Page("app/pages/modulos/academico/estudiantes/asignacion_aulas.py", title=f"{i18n._("menu.asignacion_aulas")}", icon=":material/aq_indoor:"),
        ],
        f"{i18n._("menu.administracion")}": [
            st.Page("app/pages/modulos/academico/administracion/ciclos_escolares.py", title=f"{i18n._("menu.ciclos_escolares")}", icon=":material/cycle:"),
            st.Page("app/pages/modulos/academico/administracion/niveles.py", title=f"{i18n._("menu.niveles")}", icon=":material/floor:"),
            st.Page("app/pages/modulos/academico/administracion/cursos.py", title=f"{i18n._("menu.cursos")}", icon=":material/holiday_village:"),
            st.Page("app/pages/modulos/academico/administracion/areas_tematicas.py", title=f"{i18n._("menu.areas_tematicas")}", icon=":material/theater_comedy:"),
            st.Page("app/pages/modulos/academico/administracion/asignaturas.py", title=f"{i18n._("menu.asignaturas")}",  icon=":material/book:"),
            st.Page("app/pages/modulos/academico/administracion/formulas_parciales.py", title=f"{i18n._("menu.formulas_parciales")}", icon=":material/function:"),
            st.Page("app/pages/modulos/academico/administracion/parciales.py", title=f"{i18n._("menu.parciales")}", icon=":material/hdr_weak:"),
            st.Page("app/pages/modulos/academico/administracion/capacitaciones.py", title=f"{i18n._("menu.capacitaciones")}",  icon=":material/school:"),
            st.Page("app/pages/modulos/academico/administracion/bloques_horario.py", title=f"{i18n._("menu.bloques_horario")}", icon=":material/calendar_clock:"),
        ],
        f"{i18n._("menu.configuracion")}": [
            st.Page("app/pages/mi_perfil.py", title=f"{i18n._("menu.mi_perfil")}", icon=":material/account_circle:"),
            st.Page("app/pages/manage_account.py", title=f"{i18n._("menu.configuracion")}", icon=":material/account_circle:"),
        ]
    }
    
    return pages

    