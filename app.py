import streamlit as st
import google.generativeai as genai

# 1. Configuração de Layout
st.set_page_config(
    page_title="NinjaBrain OS", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. Conexão com a API
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("Erro ao carregar a chave API nos Secrets.")

# 3. Personalidade Híbrida
system_prompt = (
    "Você é o NinjaBrain OS. "
    "MODO MENTOR: Ajuda em vida, finanças e produtividade. "
    "MODO PRD ARCHITECT: Transforma ideias em Documentos de Requisitos (PRD) técnicos "
    "e gera o código inicial pronto para o Cursor Free."
)

# 4. Inicialização do Modelo (Alterado para gemini-pro para maior compatibilidade)
model = genai.GenerativeModel(
    model_name="gemini-pro",
    system_instruction=system_prompt
)

# 5. Barra Lateral
with st.sidebar:
    st.title("🥷 Ferramentas")
    modo = st.radio("Foco:", ["🧠 Mentor de Vida", "🛠️ Arquiteto de PRD"])
    st.divider()
    upload = st.file_uploader("Subir arquivo", type=['pdf', 'png', 'jpg', 'mp3'])

# 6. Chat Interface
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
            input_text = prompt
            if modo == "🛠️ Arquiteto de PRD":
                input_text = f"Gere um PRD e o código para: {prompt}"
            
            # Nota: O modelo 'gemini-pro' padrão pode ter limitações com arquivos diretamente no prompt
            # Se precisar de multimodal, o ideal é o 1.5-flash ou 1.5-pro assim que liberados na sua conta
            response = model.generate_content(input_text)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Erro na geração: {e}")
            st.info("Tente simplificar o pedido ou verifique se o modelo está ativo na sua região.")