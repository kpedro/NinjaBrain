import streamlit as st
import google.generativeai as genai

# 1. Configuração inicial
st.set_page_config(page_title="NinjaBrain OS", layout="wide")

# 2. Conexão com a API (Pega a chave dos Secrets)
if "GEMINI_API_KEY" not in st.secrets:
    st.error("ERRO: Chave GEMINI_API_KEY não encontrada nos Secrets.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Barra Lateral (Onde estarão os botões)
with st.sidebar:
    st.title("🥷 Ferramentas")
    st.success("Modo: Mentor de Vida")
    st.divider()
    arquivo = st.file_uploader("Subir Arquivo", type=['pdf', 'png', 'jpg'])
    st.divider()
    st.subheader("📥 Exportar")

# 4. Chat Principal
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
            # Teste de resposta simples
            res = model.generate_content(prompt)
            resposta = res.text
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})
            
            # ATIVA OS BOTÕES DE EXPORTAR
            with st.sidebar:
                st.download_button("📥 Baixar TXT", resposta, file_name="ninja.txt")
                st.download_button("📄 Salvar Word", resposta, file_name="ninja.doc")
        except Exception as e:
            st.error(f"Erro: {e}")