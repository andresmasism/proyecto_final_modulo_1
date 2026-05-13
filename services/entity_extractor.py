try:
    from .gemini_service import get_gemini_client
except ImportError:
    from services.gemini_service import get_gemini_client

import json

def extract_entities(text, custom_api_key=None):
    """Extrae entidades y conceptos clave de forma generalizada."""
    if custom_api_key:
        from google import genai
        client = genai.Client(api_key=custom_api_key)
    else:
        client = get_gemini_client()
    
    prompt = f"""
    Actúa como un analista de datos experto. Analiza el siguiente texto y extrae TODA la información relevante.
    Texto: '{text}'
    
    Responde ÚNICAMENTE en formato JSON con estas llaves:
    - entidades_clave: (Personas, organizaciones, lugares o marcas)
    - conceptos_tecnicos: (Tecnologías, metodologías o términos especializados)
    - fechas_y_eventos: (Cualquier referencia temporal o sucesos clave)
    - temas_principales: (Lista de los 3 temas o ideas centrales del texto)
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    raw_json = response.text.replace('```json', '').replace('```', '').strip()
    return json.loads(raw_json)