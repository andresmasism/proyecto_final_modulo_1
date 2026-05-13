try:
    from .gemini_service import get_gemini_client
except ImportError:
    from services.gemini_service import get_gemini_client

import os
import time
from google import genai

def process_document_chat(uploaded_file, user_query, custom_api_key=None):
    """Procesa archivos usando Google File API corrigiendo el parámetro de carga."""
    temp_path = None
    uploaded_gemini_file = None
    try:
        if custom_api_key:
            client = genai.Client(api_key=custom_api_key)
        else:
            client = get_gemini_client()

        # 1. Guardar archivo localmente de forma temporal
        temp_path = f"temp_{os.urandom(4).hex()}_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 2. Subir a Google File API (Corregido: 'file' en lugar de 'path')
        uploaded_gemini_file = client.files.upload(file=temp_path)

        # Esperar brevemente a que el archivo sea procesado por Google
        while uploaded_gemini_file.state.name == "PROCESSING":
            time.sleep(1)
            uploaded_gemini_file = client.files.get(name=uploaded_gemini_file.name)

        if uploaded_gemini_file.state.name == "FAILED":
            raise Exception("La carga del archivo a la API de Google falló.")

        # 3. Generar respuesta
        prompt = f"""
        Actúa como un asistente de lectura experto. Analiza el documento proporcionado y responde a la siguiente pregunta basándote únicamente en su contenido.

        Pregunta: {user_query}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[uploaded_gemini_file, prompt]
        )
        
        return response.text

    except Exception as e:
        if "403" in str(e):
            return "❌ Error 403: La API Key no tiene permisos para File API (Verifica Google AI Studio)."
        return f"❌ Error en RAG Service: {str(e)}"
    finally:
        # Limpieza local
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)