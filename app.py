import streamlit as st
import google.generativeai as genai

# 1. Configuração e Estilo
st.set_page_config(page_title="NinjaBrain Pro", layout="wide")

# Conexão com a chave nos Secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# 2. BARRA LATERAL (Abas de Funções)
with st.sidebar:
    st.title("🧰 Ferramentas Ninja")
    
    tab_upload, tab_export = st.tabs(["📁 Upload", "📤 Exportar"])
    
    with tab_upload:
        st.subheader("Analisar Arquivo")
        arquivo = st.file_uploader(
            "Subir Áudio, Imagem ou PDF", 
            type=['pdf', 'png', 'jpg', 'jpeg', 'mp3', 'wav']
        )
        if arquivo:
            st.info(f"Arquivo '{arquivo.name}' pronto para análise.")

    with tab_export:
        st.subheader("Salvar Conversa")
        # Aqui ficarão os botões de download após gerar a resposta

# 3. INTERFACE DE CHAT
st.title("🥷 NinjaBrain: Segundo Cérebro")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. LÓGICA DE PROCESSAMENTO
if prompt := st.chat_input("O que vamos evoluir hoje, Kadson?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Se tiver arquivo, o Ninja lê o arquivo + o texto
        if arquivo:
            res = model.generate_content([prompt, arquivo])
        else:
            res = model.generate_content(prompt)
        
        texto_resposta = res.text
        st.markdown(texto_resposta)
        st.session_state.messages.append({"role": "assistant", "content": texto_resposta})

        # Adiciona botões de exportação dinâmicos na aba de exportar
        with tab_export:
            st.download_button("📥 Baixar TXT", texto_resposta, file_name="ninja_brain.txt")
            st.download_button("📄 Baixar Word (Doc)", texto_resposta, file_name="ninja_brain.doc")