import requests as r
import streamlit as st
import logging
import time


# Configuración básica del logger
logging.basicConfig(
    filename="app_errors.log",  # Archivo donde se guardarán los errores
    level=logging.ERROR,        # Nivel de registro
    format="%(asctime)s - %(levelname)s - %(message)s"  # Formato del mensaje
)





url_base = "https://flask-service-999505570378.us-central1.run.app/api/v1"
HEADERS = {
    "Content-Type": "application/json",
}


def api_request(
    endpoint, 
    method="GET", 
    params=None, 
    body_params=None, 
    headers=None, 
    timeout=1800,
    is_signIn=False,
    retry=False
):
    """Función genérica con reintento automático tras refrescar token."""

    try:
        # Construir headers locales (no modificar HEADERS global)
        request_headers = HEADERS.copy()
        if not is_signIn:
            request_headers["Authorization"] = f"Bearer {st.session_state.accessToken}"

        url = f"{url_base}/{endpoint}"

        response = r.request(
            method, url,
            params=params,
            json=body_params,
            headers=request_headers,
            timeout=timeout
        )
        print(f"endpoint {endpoint}, status_code {response.status_code}")
        # --- validar respuesta JSON ---
        if not response.headers.get("Content-Type", "").startswith("application/json"):
            logging.error(f"Non-JSON response: {response.text}")
            return {"error": "Non-JSON response"}
       
        # --- respuestas exitosas ---
        if response.status_code in (200, 201):
            return response.json()
        
        if response.status_code == 440: #session expirada por inactividad
            
            st.session_state.force_login = True
            st.rerun()
            return {"error": response.json()}

        # -----------------------------------
        # ---------------------
        #  MANEJO DE 401 + REFRESH TOKEN
        # --------------------------------------------------------
        if response.status_code == 401:
            data = response.json()
            if data.get("msg") == "Token has expired" and not retry:
                refresh_headers = {
                    "Authorization": f"Bearer {st.session_state.refreshToken}"
                }
                refresh_url = f"{url_base}/auth/refresh"
                refresh_response = r.post(refresh_url, headers=refresh_headers)
                
                if refresh_response.status_code in (440, 401): #session expirada por inactividad
                    st.session_state.force_login = True
                    st.rerun()
                    return {"error": refresh_response.json()}
                
        
                if refresh_response.status_code == 200:
                    new_data_response = refresh_response.json()
                    new_data = new_data_response.get('result', None)
                    if new_data:
                        st.session_state.accessToken = new_data["accessToken"]

                        # Reintentar la llamada original una sola vez
                        return api_request(
                            endpoint, method, params, body_params,
                            headers, timeout, is_signIn, retry=True
                        )

                    
        # --- errores genéricos ---
        logging.error(f"Error occurred: {response.json()}")
        return {"error": response.json()}

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return {"error": str(e)}





