import streamlit as st
import google.generativeai as genai

# Layout e Configuração
st.set_page_config(page_title="NinjaBrain OS", layout="wide")

# Inicialização segura da API
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Configure a GEMINI_API_KEY nos Secrets do Streamlit.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Interface lateral
with st.sidebar:
    st.title("🥷 Ferramentas")
    modo = st.radio("Foco:", ["🧠 Mentor", "🛠️ Arquiteto PRD"])

# Modelo padrão (sem v1beta forçado)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title(f"🚀 NinjaBrain: {modo}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Diga algo..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Comando direto sem histórico complexo para testar conexão
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Erro: {e}")