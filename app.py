import streamlit as st
import google.generativeai as genai

# 1. Configuração Básica
st.set_page_config(page_title="NinjaBrain OS", layout="wide")

# 2. Conexão Segura
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("Erro nos Secrets: Verifique se GEMINI_API_KEY está configurada.")

# 3. Inicialização do Modelo (Usando a versão 1.0 para compatibilidade total)
try:
    # Mudança estratégica para a versão 1.0 pro
    model = genai.GenerativeModel(model_name="gemini-1.0-pro")
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")

# 4. Barra Lateral
with st.sidebar:
    st.title("🥷 Ferramentas")
    modo = st.radio("Foco:", ["🧠 Mentor de Vida", "🛠️ Arquiteto de PRD"])
    st.divider()
    st.info("O modo Multimodal (arquivos) requer modelos 1.5. No momento, use apenas texto para estabilidade.")

# 5. Chat Interface
st.title(f"🚀 NinjaBrain: {modo}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Como vamos evoluir hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Construindo o contexto manualmente para o modelo 1.0
            contexto = "Você é o NinjaBrain OS. "
            if modo == "🛠️ Arquiteto de PRD":
                prompt_final = f"{contexto} Atue como Arquiteto de PRD. Gere o plano e código para: {prompt}"
            else:
                prompt_final = f"{contexto} Atue como Mentor de Vida e Carreira. Ajude com: {prompt}"

            response = model.generate_content(prompt_final)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Erro técnico: {e}")
            st.warning("Dica: Se o erro for 404, sua chave pode precisar ser gerada novamente no Google AI Studio.")