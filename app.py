import streamlit as st
import google.generativeai as genai

# 1. Configuração de Layout
st.set_page_config(page_title="NinjaBrain OS", layout="wide", initial_sidebar_state="expanded")

# 2. Conexão com a API
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Configure a GEMINI_API_KEY nos Secrets do Streamlit.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Inicialização do Modelo (O mais estável de todos)
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. Barra Lateral com Ferramentas
with st.sidebar:
    st.title("🧰 Ferramentas Ninja")
    st.info("🎯 Modo: Mentor de Vida")
    st.divider()
    arquivo = st.file_uploader("Subir PDF ou Imagem", type=['pdf', 'png', 'jpg'])
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
            # Chamada simplificada para evitar erro v1beta
            if arquivo:
                res = model.generate_content([prompt, arquivo])
            else:
                res = model.generate_content(prompt)
            
            resposta = res.text
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})
            
            # BOTÕES DE EXPORTAÇÃO NA SIDEBAR
            with st.sidebar:
                st.download_button("📥 Baixar TXT", resposta, file_name="ninja.txt")
                st.download_button("📄 Salvar Word", resposta, file_name="ninja.doc")
                
        except Exception as e:
            st.error(f"Erro: {e}")