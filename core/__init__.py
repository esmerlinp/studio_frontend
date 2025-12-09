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





url_base = "http://127.0.0.1:5000"
HEADERS = {
    "Content-Type": "application/json",
}


def fetch_data(endpoint, method="GET", params=None, body_params=None, headers=None, timeout=1800, is_singIn=False):
    """
    Función genérica para realizar solicitudes HTTP.

    :param endpoint: Endpoint de la API.
    :param method: Método HTTP (GET, POST, etc.).
    :param params: Parámetros de consulta.
    :param body_params: Datos del cuerpo de la solicitud.
    :param headers: Encabezados adicionales.
    :param timeout: Tiempo de espera en segundos.
    :return: Respuesta en formato JSON o texto.
    """


    try:
        
        HEADERS["Authorization"] = f"Bearer {st.session_state.accessToken}"

        url = f"{url_base}/{endpoint}"
        response = r.request(method, url, params=params, json=body_params, headers=HEADERS, timeout=timeout)

   
    
        if not response.headers.get("Content-Type", "").startswith("application/json"):
            logging.error(f"Non-JSON response: {response.text}")
            return {"error": "Non-JSON response"}
        
        
         
        if response.status_code in (200, 201):
            return response.json()
            
        if response.status_code == 401:
            data = response.json()
            
            if data.get("msg") == "Token has expired":
                #print(data.get("msg"))
                #return None
                headers = {"Authorization": st.session_state.refreshToken}
                
                url = f"{url_base}/refresh"
                result = r.request("POST", url, headers=headers)
                
                if result:
                    data = result.json()
                    st.session_state["accessToken"] = data['accessToken']
                    st.session_state.update_token = True
                    
        data_error = response.json()
        return {"error": data_error}
        #return response.json()
    
    except Exception as e:
        logging.error(f"Error occurred: {e}")  # Registrar el error HTTP
        return {"error": e}





def login(user_name:str, password:str):
    
    Credencials = {
        "username": user_name,
        "password": password
    }
    
    response = fetch_data(endpoint="/login", method="POST", body_params=Credencials)
    print(response)
    data = response.get("result", None)
    
    if data:
        st.session_state.accessToken = data['accessToken']
        st.session_state.refreshToken = data['refresh_token']
        #st.session_state.is_auth = "True"
        st.session_state.user = data
        
        
    
    return data

def log_out():
    
    return True