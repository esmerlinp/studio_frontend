import streamlit as st
from app.utils import i18n
from app.services.auth_service import login

def login_form(cookies):
    # Custom CSS for the login card
    st.markdown("""
        <style>
        .login-container {
            margin-top: 5rem;
        }
        div[data-testid="stForm"] {
            background-color: white;
            padding: 3rem;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            border: 1px solid #e0e0e0;
        }
        .stTextInput > label {
            font-weight: 500;
            color: #333;
        }
        .stButton > button {
            width: 100%;
            border-radius: 6px;
            font-weight: 600;
            background-color: #0c0c0c; /* Example primary color */
            color: white;
        }
        .login-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .login-header h1 {
            font-size: 1.8rem;
            font-weight: 700;
            color: #1a1a1a;
            margin: 0;
        }
        .login-header p {
            color: #666;
            margin-top: 0.5rem;
            font-size: 0.95rem;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.5, 1, 1.5])
    
    with col2:
        st.markdown('<div class="login-container"></div>', unsafe_allow_html=True)
        with st.form("login_form", enter_to_submit=True, clear_on_submit=False, border=False):
            st.markdown("""
                <div class="login-header">
                    <h1>AKDMIA</h1>
                    <p>Bienvenido de nuevo</p>
                </div>
            """, unsafe_allow_html=True)
            
            username = st.text_input(f"{i18n._('login.username')}", placeholder="ejemplo@usuario.com")
            password = st.text_input(f"{i18n._('login.password')}", type="password", placeholder="••••••••")
            
            st.markdown(" <br>", unsafe_allow_html=True) # Spacer
            submit_button = st.form_submit_button("Iniciar Sesión", type="primary")
            
            # Additional visual feedback
            if submit_button:
                data_auth = login(user_name=username, password=password)
                if data_auth:
                    cookies["is_auth"] = str(True)
                    cookies["accessToken"] = data_auth.accessToken
                cookies["refreshToken"] = data_auth.refresh_token
                cookies["me"] = str(data_auth.__dict__)
                cookies.save()
                st.rerun()
            else:
                st.warning(f"{i18n._('login.error_empty_fields')}")
                st.stop()
            