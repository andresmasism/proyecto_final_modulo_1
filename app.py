import streamlit as st
import base64

from services.gaslight_service import generate_response
from services.classifier_service import classify_ticket
from services.entity_extractor import extract_entities
from services.rag_service import process_document_chat

# --- VARIABLE GLOBAL API KEY ---
user_api_key = None

# --- FUNCIÓN PARA CARGAR IMAGEN LOCAL --- 
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🚀",
    layout="wide"
)

# --- BACKGROUND ---
try:
    bin_str = get_base64_of_bin_file('assets/background.png')

    bg_style = f"""
        background-image:
        linear-gradient(rgba(18, 18, 18, 0.82), rgba(18, 18, 18, 0.82)),
        url("data:image/png;base64,{bin_str}");
    """

except FileNotFoundError:
    bg_style = "background-color: #121212;"

# --- CSS PERSONALIZADO ---
st.markdown(f"""
<style>

.stApp {{
    {bg_style}
    background-size: cover;
    background-position: right 20%;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: #e0e0e0;
}}

/* Tabs distribuidos equitativamente */
button[data-baseweb="tab"] {{
    flex-grow: 1;
    text-align: center;
}}

/* Botones */
.stButton>button {{
    border-radius: 8px;
    height: 3.5em;
    background-color: #2e7d32;
    color: white;
}}

/* Inputs */
.stTextArea textarea,
.stTextInput input {{
    background-color: rgba(45,45,45,0.7) !important;
    color: white !important;
}}

/* Header transparente */
header {{
    background: transparent !important;
}}

</style>
""", unsafe_allow_html=True)

# --- BOTÓN FLOTANTE CONFIGURACIÓN ---
left, middle, right = st.columns([1, 20, 1])

with left:
    with st.popover("⚙️"):

        st.markdown("## Configuración")

        st.info(
            "Bienvenido a AI Assistant.\n\n"
            "Esta herramienta utiliza Gemini 2.5 y modelos de Hugging Face."
        )

        user_api_key = st.text_input(
            "Gemini API Key:",
            type="password",
            help="Si dejas esto vacío, solo podras usar el System Ticketing. Crea una API Key en Google AI Studio y pégala aquí para acceder a todas las funcionalidades."
        )

        st.divider()

        st.markdown("### Estado del Sistema")

        st.success("Conectado a Hugging Face Hub")

        if user_api_key:
            st.success("API Key personalizada activa")

# --- ENCABEZADO ---
st.title("AI Assistant: Asistente Multitarea")
st.caption("Inteligencia Artificial Integrada para Productividad y Creatividad")

# --- ESTADO INICIAL ---
if "show_tabs" not in st.session_state:
    st.session_state.show_tabs = False

# =========================================================
# LANDING CONTENT
# =========================================================

    st.markdown(
        """
        <h2 style='text-align: center;'>
            Bienvenido a AI Assistant
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

# =========================================================
# SECCIONES CENTRADAS
# =========================================================

    left_space, content, right_space = st.columns([1, 3, 1])

    with content:

        row1_col1, row1_col2 = st.columns(2)

        with row1_col1:

            st.markdown("""
            ### ✨ Creative Hub
            
            Generación creativa y respuestas humorísticas.
            """)

        with row1_col2:

            st.markdown("""
            ### 📊 Smart Ticketing
            
            Clasificación automática de tickets de soporte.
            """)

        st.write("")

        row2_col1, row2_col2 = st.columns(2)

        with row2_col1:

            st.markdown("""
            ### 🔍 Knowledge Extraction
            
            Extracción inteligente de entidades y conceptos.
            """)

        with row2_col2:

            st.markdown("""
            ### 📄 AI Document Chat
            
            Conversa con documentos PDF o TXT usando Gemini.
            """)

# =========================================================
# BOTÓN CENTRADO
# =========================================================

    st.write("")
    st.write("")

    left_btn, center_btn, right_btn = st.columns([2,1,2])

    with center_btn:

        if st.button("Comenzar 🚀"):

            st.session_state.show_tabs = True
            st.rerun()

# =========================================================
# APP PRINCIPAL
# =========================================================

else:

# --- TABS ---
    tab1, tab2, tab3, tab4 = st.tabs([
        "✨ Creative Hub", 
        "📊 Smart Ticketing", 
        "🔍 Knowledge Extraction", 
        "📄 AI Document Chat"
    ])

    with tab1:

        st.subheader("Generador de Lenguaje Creativo")

        with st.expander("💡 ¿Cómo funciona?", expanded=False):
            st.write(
                "Usa el modo **Excusa** para situaciones profesionales "
                "o **Gaslight** para respuestas humorísticas y absurdas."
            )

        col_left, col_right = st.columns([1, 2])

        with col_left:
            opcion = st.radio(
                "Estilo de respuesta:",
                ["Excusa Creativa", "Modo Gaslight"]
            )

        with col_right:
            situacion = st.text_area(
                "Describe la situación:",
                placeholder="Ej: Llegué tarde a la reunión..."
            )

        if st.button("Generar Respuesta ✨"):

            if situacion:

                with st.spinner("Tejiendo realidad alternativa..."):

                    try:
                        mode_key = (
                            "gaslight"
                            if opcion == "Modo Gaslight"
                            else "excusa"
                        )

                        res = generate_response(
                            situacion,
                            mode=mode_key,
                            custom_api_key=user_api_key or None
                        )

                        st.chat_message("assistant").write(res)

                    except Exception as e:
                        st.error(f"Error: {e}")

    with tab2:
        st.subheader("Clasificación Inteligente de Soporte")
        ticket_text = st.text_area("Mensaje del Cliente:", height=150, placeholder="Pega aquí el correo o mensaje del usuario...")

        if st.button("Ejecutar Análisis 📊"):
            if ticket_text:
                with st.status("Analizando ticket...", expanded=True) as status:
                    st.write("Cargando modelos BART y BETO...")
                    res = classify_ticket(ticket_text)
                    status.update(label="¡Análisis completado!", state="complete", expanded=False)
                
                m1, m2, m3 = st.columns(3)
                m1.metric("Categoría", res['categoria'])
                m2.metric("Prioridad", res['prioridad'])
                m3.metric("Tono Detectado", res['humor'])
                
                st.markdown(f"> **Resumen Ejecutivo:** {res['resumen']}")
                st.caption(f"Nivel de confianza: {res['confianza']}")

    with tab3:
        st.subheader("Extractor de Entidades y Conceptos")
        data_text = st.text_area("Texto a Procesar:", height=200, placeholder="Cualquier artículo, noticia o documento...")
        
        if st.button("Extraer Data 🔍"):
            if data_text:
                with st.spinner("Consultando a la IA..."):
                    try:
                        info = extract_entities(data_text, custom_api_key=user_api_key or None)
                        cols = st.columns(2)
                        idx = 0
                        for cat, items in info.items():
                            with cols[idx % 2]:
                                with st.container(border=True):
                                    st.markdown(f"**{cat.replace('_', ' ').upper()}**")
                                    st.write(items if items else "Sin resultados")
                            idx += 1
                    except Exception as e: st.error(f"Error: {e}")

    with tab4:
        st.subheader("Chat con Documentos")
        st.info("Sube un archivo y la IA responderá basándose únicamente en su contenido.")
        
        up_col, query_col = st.columns([1, 2])
        with up_col:
            uploaded_file = st.file_uploader("Archivo (PDF/TXT)", type=['pdf', 'txt'])
        with query_col:
            user_query = st.text_input("Tu pregunta:", placeholder="¿Qué dice el documento sobre...?")

        if st.button("Analizar Documento 📄"):
            if uploaded_file and user_query:
                with st.spinner("Leyendo archivo..."):
                    try:
                        answer = process_document_chat(uploaded_file, user_query, custom_api_key=user_api_key or None)
                        st.success("Respuesta encontrada:")
                        st.markdown(answer)
                    except Exception as e: st.error(f"Error en RAG: {e}")
            else:
                st.warning("Falta el archivo o la pregunta.")
