### 📄 Especificaciones Técnicas: AI Assistant

**1. Enlaces del Proyecto**
- **🚀 App Desplegada:** [Hugging Face Spaces](https://huggingface.co/spaces/andresmasism/AI_Asistente_Multitarea)
- **💻 Código Fuente:** [Repositorio GitHub](https://github.com/andresmasism/proyecto_final_modulo_1)

**2. Objetivo del Proyecto**
Desarrollar un asistente inteligente multitarea de alto rendimiento que centralice procesos de negocio (soporte, extracción) y herramientas creativas en una interfaz unificada.

**3. Arquitectura de Software**
- **Frontend:** Streamlit (Layout Wide, Tab-based navigation).
- **Backend:** Arquitectura modular basada en servicios (`services/`).
- **Modelos de IA:**
  - **Generación/RAG:** Google Gemini 2.5 Flash (Multimodal).
  - **NLP Especializado:** Hugging Face (BART para clasificación, BETO para sentimiento).

**4. Funcionalidades del App**
- **Creative Hub:** Generación de respuestas humorísticas (Gaslight) o excusas profesionales mediante ingeniería de prompts avanzada.
- **Smart Ticketing:** Análisis en tiempo real de tickets de soporte para determinar categoría, prioridad y el estado emocional del cliente.
- **Knowledge Extraction:** Procesamiento de texto desestructurado para extraer entidades (marcas, fechas, temas) en formato JSON.
- **Document RAG:** Consulta inteligente de archivos PDF/TXT permitiendo al usuario 'chatear' con sus propios documentos.

**5. Flujo del Usuario**
1. **Autenticación:** El usuario ingresa su propia Gemini API Key en el sidebar para uso de los servicios de IA.
2. **Selección de Tarea:** Navegación a través de los Tabs especializados según la necesidad.
3. **Entrada de Datos:** Carga de texto manual o subida de archivos (PDF/TXT) en la sección de RAG.
4. **Procesamiento:** Activación de los servicios mediante botones de acción que disparan llamadas a APIs de Google o modelos locales de Hugging Face.
5. **Visualización:** Presentación de resultados mediante métricas visuales, cuadros de texto formateados o respuestas de chat.

**6. Estructura de Archivos**
```
├── app.py                # Aplicación principal (UI)
├── assets                # Fondo de pantalla del proyecto
│   ├── background.png    # Imagen de fondo
├── Dockerfile            # Instrucciones de Docker
├── README.md             # Descripción del proyecto
├── requirements.txt      # Dependencias (transformers, streamlit, google-genai, etc.)
├── services/
│   ├── __init__.py       # Marcador de paquete
│   ├── gemini_service.py
│   ├── classifier_service.py
│   ├── gaslight_service.py
│   ├── entity_extractor.py
│   └── rag_service.py
```

**7. Instalación y Ejecución Local**

Sigue estos pasos para ejecutar el proyecto en tu máquina:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/andresmasism/proyecto_final_modulo_1.git
   cd proyecto_final_modulo_1
   ```
2. **Crear entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```
3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecutar App:**
   ```bash
   streamlit run app.py
   ```

