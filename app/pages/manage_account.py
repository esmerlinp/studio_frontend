import streamlit as st
import requests
from util import i18n
st.set_page_config(
    page_title="Client Settings",
    layout="wide"
)


# -------------------------------
#   Simular carga desde API/DB
# -------------------------------

def get_client_preferences(client_id):
    """Simula obtener datos desde API o base de datos."""
    sample_data = {
        10: {
            "idle_timeout_minutes": 30,
            "password_expiration_days": 90,
            "max_login_attempts": 5,
            "refresh_token_expiration_days": 7,
            "enforce_2fa": False,
            "timezone": "America/Santo_Domingo",
            "language": "es",
            "date_format": "DD/MM/YYYY",
            "company_logo_url": "https://example.com/logo10.png",
            "modules_enabled": {
                "payroll": True,
                "recruitment": True,
                "attendance": False,
            }
        },
        20: {
            "idle_timeout_minutes": 45,
            "password_expiration_days": 60,
            "max_login_attempts": 3,
            "refresh_token_expiration_days": 10,
            "enforce_2fa": True,
            "timezone": "America/Mexico_City",
            "language": "en",
            "date_format": "MM-DD-YYYY",
            "company_logo_url": "https://example.com/logo20.png",
            "modules_enabled": {
                "payroll": False,
                "recruitment": True,
                "attendance": True,
            }
        }
    }
    return sample_data.get(client_id)


# -------------------------------
#   Selección de Cliente
# -------------------------------
st.title("Client Configuration")

client_id = st.sidebar.selectbox(
    "Select Client",
    options=[10, 20],
    format_func=lambda x: f"Client {x}"
)

prefs = get_client_preferences(client_id)

if not prefs:
    st.error("No configuration found for this client.")
    st.stop()

# -------------------------------
#   Formulario estilo GitHub
# -------------------------------
with st.form("client_form"):

    # -------------------------------------------------
    # Security Settings
    # -------------------------------------------------
    st.subheader(f"{i18n._('form.security_settings.title')}")
    st.text(f"{i18n._('form.security_settings.description')}")

    with st.container(horizontal=True):
        with st.container(horizontal=False):
            idle_timeout_minutes = st.number_input(
                f"{i18n._('form.security_settings.idle_timeout')}",
                value=prefs["idle_timeout_minutes"]
            )
            st.caption(f"{i18n._('form.security_settings.idle_timeout.caption')}")

        with st.container(horizontal=False):
            max_login_attempts = st.number_input(
                f"{i18n._('form.security_settings.max_login_attempts')}",
                value=prefs["max_login_attempts"]
            )
            st.caption(f"{i18n._('form.security_settings.max_login_attempts.caption')}")

    with st.container(horizontal=True):
        with st.container(horizontal=False):
            password_expiration_days = st.number_input(
                f"{i18n._('form.security_settings.password_expiration')}",
                value=prefs["password_expiration_days"]
            )
            st.caption(f"{i18n._('form.security_settings.password_expiration.caption')}")

        with st.container(horizontal=False):
            refresh_token_expiration_days = st.number_input(
                f"{i18n._('form.security_settings.refresh_token_expiration')}",
                value=prefs["refresh_token_expiration_days"]
            )
            st.caption(f"{i18n._('form.security_settings.refresh_token_expiration.caption')}")

    enforce_2fa = st.checkbox(
        f"{i18n._('form.security_settings.enforce_2fa')}",
        value=prefs["enforce_2fa"]
    )
    st.caption(f"{i18n._('form.security_settings.enforce_2fa.caption')}")

    st.divider()

    # -------------------------------------------------
    # Localization
    # -------------------------------------------------
    st.subheader(f"{i18n._('form.localization.title')}")
    st.text(f"{i18n._('form.localization.description')}")

    timezone = st.text_input(
        f"{i18n._('form.localization.timezone')}",
        value=prefs["timezone"]
    )
    st.caption(f"{i18n._('form.localization.timezone.caption')}")

    language = st.text_input(
        f"{i18n._('form.localization.language')}",
        value=prefs["language"]
    )
    st.caption(f"{i18n._('form.localization.language.caption')}")

    date_format = st.text_input(
        f"{i18n._('form.localization.date_format')}",
        value=prefs["date_format"]
    )
    st.caption(f"{i18n._('form.localization.date_format.caption')}")

    st.divider(width="stretch")

    # -------------------------------------------------
    # Modules
    # -------------------------------------------------
    st.subheader(f"{i18n._('form.modules.title')}")
    st.text(f"{i18n._('form.modules.description')}")

    mod_col1, mod_col2, mod_col3 = st.columns(3)
    modules_enabled = prefs["modules_enabled"]

    with mod_col1:
        payroll = st.checkbox(
            f"{i18n._('form.modules.payroll')}",
            value=modules_enabled.get("payroll")
        )

    with mod_col2:
        recruitment = st.checkbox(
            f"{i18n._('form.modules.recruitment')}",
            value=modules_enabled.get("recruitment")
        )

    with mod_col3:
        attendance = st.checkbox(
            f"{i18n._('form.modules.attendance')}",
            value=modules_enabled.get("attendance")
        )

    st.caption(f"{i18n._('form.modules.caption')}")

    st.divider(width="stretch")

    # -------------------------------------------------
    # Branding
    # -------------------------------------------------
    st.subheader(f"{i18n._('form.branding.title')}")

    company_logo_url = st.text_input(
        f"{i18n._('form.branding.company_logo_url')}",
        value=prefs["company_logo_url"]
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------------------------
    # Submit
    # -------------------------------------------------
    submit = st.form_submit_button(f"{i18n._('form.submit')}")



if submit:
    updated = {
        "cliente_id": client_id,
        "idle_timeout_minutes": idle_timeout_minutes,
        "password_expiration_days": password_expiration_days,
        "max_login_attempts": max_login_attempts,
        "refresh_token_expiration_days": refresh_token_expiration_days,
        "enforce_2fa": enforce_2fa,
        "timezone": timezone,
        "language": language,
        "date_format": date_format,
        "company_logo_url": company_logo_url,
        "modules_enabled": {
            "payroll": payroll,
            "recruitment": recruitment,
            "attendance": attendance
        }
    }

    st.success("Configuration updated!")
    st.json(updated)
