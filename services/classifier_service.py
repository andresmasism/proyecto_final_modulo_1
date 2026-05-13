from transformers import pipeline
import torch

# Cargamos los pipelines necesarios
# 1. Zero-shot para categorías
classifier = pipeline("zero-shot-classification", 
                      model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli",
                      device=0 if torch.cuda.is_available() else -1
                      )

# 2. Análisis de sentimiento (BETO es excelente para español)
sentiment_analyzer = pipeline("sentiment-analysis", 
                              model="finiteautomata/beto-sentiment-analysis",
                              device=0 if torch.cuda.is_available() else -1)

def classify_ticket(text, custom_api_key=None):
    """Analiza categoría, sentimiento y prioridad de forma unificada."""
    # A. Clasificación de Categoría
    candidate_labels = [
        "Problema Técnico o Error", 
        "Facturación y Pagos", 
        "Sugerencia o Feedback", 
        "Consulta General"
    ]
    class_res = classifier(text, candidate_labels)
    
    label_map = {
        "Problema Técnico o Error": "Técnico",
        "Facturación y Pagos": "Facturación",
        "Sugerencia o Feedback": "Feedback",
        "Consulta General": "General"
    }
    
    categoria = label_map.get(class_res['labels'][0], "Otros")
    score_cat = class_res['scores'][0]
    
    # B. Análisis de Sentimiento
    sent_res = sentiment_analyzer(text)[0]
    sentimiento_raw = sent_res['label'] # POS, NEG, NEU
    
    # Mapeo visual del humor
    sent_map = {"POS": "😊 Positivo", "NEG": "😡 Molesto", "NEU": "😐 Neutral"}
    humor = sent_map.get(sentimiento_raw, sentimiento_raw)

    # C. Lógica de Prioridad Inteligente
    # La prioridad es ALTA si el usuario está molesto (NEG) o si el score técnico es muy alto
    prioridad = "Media"
    if sentimiento_raw == "NEG" or score_cat > 0.85 or "urgente" in text.lower():
        prioridad = "Alta"
    elif sentimiento_raw == "POS" and score_cat < 0.5:
        prioridad = "Baja"

    return {
        "categoria": categoria,
        "prioridad": prioridad,
        "humor": humor,
        "confianza": f"{(score_cat * 100):.1f}%",
        "resumen": f"{text[:60]}..."
    }
