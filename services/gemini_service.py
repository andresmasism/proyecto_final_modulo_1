import streamlit as st
from google import genai
import os

def get_gemini_client():
    """Configura el cliente priorizando secretos de Streamlit para la app."""
    api_key = None
    
    # 1. Intentar obtener de Streamlit Secrets (Producción/App)
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
    
    # 2. Fallback a Google Colab Secrets (Desarrollo en Notebook)
    if not api_key:
        try:
            from google.colab import userdata
            api_key = userdata.get('GEMINI_API_KEY')
        except (ImportError, Exception):
            pass
            
    if not api_key:
        raise Exception("No se encontró GEMINI_API_KEY en st.secrets ni en Colab.")

    return genai.Client(api_key=api_key)
