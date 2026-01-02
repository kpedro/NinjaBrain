import streamlit as st
import google.generativeai as genai

# 1. Configuração Visual
st.set_page_config(page_title="NinjaBrain: Seu Mentor 360º", layout="centered")
st.title("🥷 NinjaBrain: Seu Mentor 360º")
st.caption("Especialista em Vida, IA, Finanças e Concursos")

# 2. Conexão com a Chave Secreta
# O Streamlit busca a chave que você salvou no menu 'Secrets'
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 3. A NOVA PERSONALIDADE (Onde o Ninja evolui)
system_prompt = (
    "Você é o NinjaBrain, o Mentor Pessoal do Kadson. "
    "Sua missão é ajudá-lo em TODAS as áreas da vida: "
    "1. IA e Tecnologia: Ensine-o a dominar ferramentas e automatizar tarefas. "
    "2. Carreira e Riqueza: Dê conselhos estratégicos e planos de ação. "
    "3. Concursos (CNU): Continue sendo o mestre nos estudos. "
    "4. Estilo de Vida: Ajude na organização e produtividade diária. "
    "Responda sempre de forma direta, motivadora e organizada."
)

# 4. Inicialização do Modelo
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)

# 5. Memória da Conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. O TRECHO PRINCIPAL (Interação)
if prompt := st.chat_input("Em que vamos evoluir hoje, Kadson?"):
    # Adiciona a pergunta do usuário no histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera a resposta do Mentor
    with st.chat_message("assistant"):
        # Cria o chat com o histórico atual
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt)
        
        st.markdown(response.text)
        # Salva a resposta do Ninja no histórico
        st.session_state.messages.append({"role": "assistant", "content": response.text})