import streamlit as st
from app.utils import i18n




def modules_page():
    
    # Custom CSS for Google Apps style grid
    st.markdown("""
        <style>
        .module-card {
            background-color: white;
            border: 1px solid #dadce0;
            border-radius: 8px;
            padding: 24px;
            text-align: center;
            height: 100%;
            transition: box-shadow 0.2s, transform 0.1s;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .module-card:hover {
            box-shadow: 0 4px 12px rgba(60, 64, 67, 0.15);
            border-color: transparent;
            transform: translateY(-2px);
        }
        .module-icon {
            font-size: 48px;
            margin-bottom: 16px;
        }
        .module-title {
            font-family: 'Google Sans', 'Roboto', sans-serif;
            font-size: 18px;
            font-weight: 500;
            color: #3c4043;
            margin: 0;
        }
        .module-desc {
            font-size: 12px;
            color: #5f6368;
            margin-top: 8px;
            line-height: 1.5;
        }
        /* Hide default buttons to make the whole card clickable logic work via st.button overlay or similar */
        div.stButton > button {
            width: 100%;
            border: none;
            background: transparent;
            color: transparent;
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            z-index: 2;
        }
        /* Container tweaks */
        .block-container {
            padding-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

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

    st.markdown(f"<h2 style='text-align: center; color: #202124; margin-bottom: 40px;'>{i18n._('modules.select_title')}</h2>", unsafe_allow_html=True)
    # st.write(f"{i18n._('modules.select_subtitle')}") # Optional, maybe too noisy for Google style

    # Grid Layout
    cols = st.columns(3) # 3 columns for a desktop grid feel
    
    for index, (modulo, descripcion) in enumerate(modulos.items()):
        col = cols[index % 3] # Wrap around 3 columns
        
        with col:
            # Create the visual card
            card_html = f"""
            <div class="module-card">
                <div class="module-icon">{icons.get(modulo, '📦')}</div>
                <h3 class="module-title">{modulo}</h3>
                <p class="module-desc">{descripcion}</p>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
            # Button overlay for functionality
            # Note: Streamlit buttons inside columns with custom HTML is tricky. 
            # We place a button that looks like "Acceder" below or try to make the whole area clickable.
            # To keep it simple and reliable in Streamlit:
            if st.button(f"Acceder a {modulo}", key=f"btn_{modulo}", use_container_width=True):
                 st.session_state.modulo_actual = modulo
                 st.rerun()

