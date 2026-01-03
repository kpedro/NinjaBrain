import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração de Layout
st.set_page_config(page_title="NinjaBrain OS", layout="wide", initial_sidebar_state="expanded")

# 2. Conexão Estritamente Estável (v1)
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Configure a GEMINI_API_KEY nos Secrets.")
    st.stop()

# FORÇANDO A API V1 (ESTÁVEL) - Isso mata o erro v1beta
os.environ["GOOGLE_API_VERSION"] = "v1" 
genai.configure(api_key=st.secrets["GEMINI_API_KEY"], transport='rest')

# 3. Inicialização do Modelo
# Usando o nome técnico completo que evita o erro 404
model = genai.GenerativeModel('models/gemini-1.5-flash')

# 4. Barra Lateral
with st.sidebar:
    st.title("🧰 Ferramentas Ninja")
    st.success("🎯 Modo: Mentor de Vida")
    st.divider()
    arquivo = st.file_uploader("Analisar Arquivo", type=['pdf', 'png', 'jpg'])
    st.divider()
    st.subheader("📥 Exportar")

# 5. Interface de Chat
st.title("🚀 NinjaBrain OS")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Diga algo para testar..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Chamada direta
            if arquivo:
                res = model.generate_content([prompt, arquivo])
            else:
                res = model.generate_content(prompt)
            
            resposta = res.text
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})
            
            # ATIVA OS BOTÕES DE EXPORTAR NA SIDEBAR
            with st.sidebar:
                st.download_button("📥 Baixar TXT", resposta, file_name="ninja.txt")
                st.download_button("📄 Salvar Word", resposta, file_name="ninja.doc")
                
        except Exception as e:
            st.error(f"Erro Crítico: {e}")
            st.info("Se o erro 404 persistir, troque o nome do modelo para 'models/gemini-pro'.")