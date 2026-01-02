import streamlit as st
import google.generativeai as genai

# 1. Configuração de Alta Performance
st.set_page_config(page_title="NinjaBrain OS", layout="wide", initial_sidebar_state="expanded")

# Conexão com a API
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 2. PERSONALIDADE DUPLA (Mentor + PRD Architect)
system_prompt = (
    "Você é o NinjaBrain OS, uma inteligência híbrida de alto nível. "
    "Sua missão é atuar em dois modos dependendo da necessidade do Kadson: "
    "MODO MENTOR: Ajuda em vida, finanças, estudos (CNU) e produtividade. "
    "MODO PRD ARCHITECT: Atua como um engenheiro de software sênior. Transforma ideias em "
    "Documentos de Requisitos (PRD) técnicos. Quando solicitado um app, você deve entregar: "
    "1. Objetivo; 2. Funcionalidades; 3. Tech Stack; 4. O Código pronto para o Cursor Free."
)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)

# 3. INTERFACE COM ABAS E SIDEBAR
with st.sidebar:
    st.title("🥷 Ferramentas")
    modo = st.radio("Escolha o Foco:", ["🧠 Mentor de Vida", "🛠️ Arquiteto de PRD (Apps)"])
    st.divider()
    upload = st.file_uploader("Subir arquivo (PDF, Imagem, Áudio)", type=['pdf', 'png', 'jpg', 'mp3', 'wav'])
    if upload:
        st.success("Arquivo pronto!")

# 4. ÁREA DE CHAT
st.title(f"🚀 NinjaBrain: {modo}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("O que vamos construir ou resolver hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Contexto extra se estiver no modo PRD
        if modo == "🛠️ Arquiteto de PRD (Apps)":
            prompt = f"Gere um PRD completo e o código inicial para esta ideia: {prompt}"
        
        # Processamento multimodal
        if upload:
            response = model.generate_content([prompt, upload])
        else:
            response = model.generate_content(prompt)
            
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
        # Botões de Exportação na barra lateral após a resposta
        with st.sidebar:
            st.download_button("📥 Baixar Resposta (TXT)", response.text, file_name="ninja_output.txt")