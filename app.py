import streamlit as st
import google.generativeai as genai
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="NinjaBrain Multimodal", layout="wide")
st.title("🥷 NinjaBrain: Segundo Cérebro Pro")

# Conexão segura
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# --- BARRA LATERAL (Uploads e Exportação) ---
with st.sidebar:
    st.header("📁 Central de Arquivos")
    uploaded_file = st.file_uploader("Subir Áudio, Imagem ou PDF", type=['pdf', 'png', 'jpg', 'jpeg', 'mp3', 'wav'])
    
    if uploaded_file:
        st.success(f"Arquivo {uploaded_file.name} carregado!")

# --- ÁREA DE CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ninja, analise este arquivo para mim..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Lógica para processar arquivos + texto
        if uploaded_file:
            content = [prompt, uploaded_file]
            response = model.generate_content(content)
        else:
            response = model.generate_content(prompt)
        
        full_response = response.text
        st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

        # --- BOTÕES DE EXPORTAÇÃO ---
        col1, col2 = st.columns(2)
        with col1:
            st.download_button("📥 Baixar TXT", full_response, file_name="resposta_ninja.txt")
        with col2:
            # Simulação simples de Word via texto puro
            st.download_button("📄 Exportar Word (Doc)", full_response, file_name="resposta_ninja.doc")