### 📄 Especificaciones Técnicas: AI Assistant

**1. Enlaces del Proyecto**
- **💻 Código Fuente:** [Repositorio GitHub](https://github.com/andresmasism/proyecto_final_modulo_1)
- **🎈 App desplegada en Streamlit:** [Streamlit Cloud](https://proyectofinalmodulo1-ai-assistant.streamlit.app)
- **🚀 App Desplegada en HuggingFace:** [Hugging Face Spaces](https://huggingface.co/spaces/andresmasism/AI_Asistente_Multitarea)

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

**8. Galería de la Aplicación**
*Capturas de pantalla del app funcionando*

- **🚀 Interfaz Principal**

![Main Interface](https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/Landing%20Page.png) 

- **⚙️ Configuración**

Al hacer click en el ícono de configuración se desplegará la siguiente imagen.
<p align="center">
  <img 
    src="https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/Config%20Menu.png"
    width="50%"
  >
</p>

Al ingresar el API Key personalizada para utilizar Gemini se verá el estado como activada de la misma.
<p align="center">
  <img 
    src="https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/Config%20Menu%202.png"
    width="50%"
  >
</p>

- **✨ Creative Hub**

Al escoger la opción de excusa y colocar la situación al presionar generar respuesta se desplegará la siguiente imagen.


![Creative Hub 1](https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/Creative%20Hub%20.png) 

Al escoger la opción de gaslight y colocar la situación al presionar generar respuesta se desplegará la siguiente imagen.

![Creative Hub 2](https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/Creative%20Hub%202.png) 

- **📊 Smart Ticketing**

A continuación se muestran dos opciones de respuesta para posibles situaciones suministradas por el usuario.

![smart ticket 1](https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/Smart%20Ticketing.png)

![smart ticket 2](https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/Smart%20Ticketing%202.png)

- **🔍 Knowledge Extraction**

Al ingresar un texto se procedera a analizar los diferentes conceptos y entidades del mismo.

![knowledge 1](https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/Knowledge%20Extraction.png)

Mostrando la salida como en la siguiente imagen con información relevante del texto.

![knowledge 2](https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/Extracted%20Knowledge.png)

- **📄 AI Document Chat**

En la última pestaña se tiene la opción de agregar documentos en formato txt o pdf y pedirle a la IA que conteste preguntas del mismo.

![ai doc 1](https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/AI%20Document%20Chat.png)

Ejemplo con un documento txt.

![ai doc 1](https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/AI%20Document%20Chat%202.png)

Ejemplo de un documento pdf.

![ai doc 1](https://raw.githubusercontent.com/andresmasism/proyecto_final_modulo_1/refs/heads/master/assets/AI%20Document%20Chat%203.png)
