from services.gemini_service import get_gemini_client
from google import genai

def generate_response(text, mode="excusa", custom_api_key=None):
    """Genera una respuesta única y creativa usando Gemini 2.5."""
    # Si hay una llave manual, creamos un cliente temporal
    if custom_api_key:
        client = genai.Client(api_key=custom_api_key)
    else:
        client = get_gemini_client()

    if mode == "gaslight":
        role_instruction = "Eres un experto en gaslighting. Tu objetivo es convencer al usuario de que lo que pregunta nunca pasó, que su memoria falla o que la realidad es distinta."
    else:
        role_instruction = "Eres un generador de excusas profesionales. Tu objetivo es inventar una razón externa por la cual no se pudo cumplir con algo, siempre manteniendo un tono inocente y profesional."

    prompt = f"""
    {role_instruction}
    
    Entrada del usuario: '{text}'
    
    Instrucciones: Genera UNA SOLA respuesta corta (máximo 2 frases). 
    No menciones que eres una IA. Sé directo y creativo.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()
