import streamlit as st
from app.utils import i18n




def modules_page():
    
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

