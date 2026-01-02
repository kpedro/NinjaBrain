import streamlit as st
import google.generativeai as genai
import os

# Configuração da página para ficar com cara de Dashboard
st.set_page_config(page_title="NinjaBrain: Life & AI Mentor", layout="centered")

# Puxa a chave que você salvou no Streamlit Cloud
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# AQUI ESTÁ O "CÉREBRO" QUE VOCÊ NÃO ACHAVA:
# Definimos a nova personalidade do Ninja
system_prompt = (
    "Você é o NinjaBrain, o Mentor Pessoal do Kadson. "
    "Sua missão é ajudá-lo em TODAS as áreas da vida: "
    "1. IA e Tecnologia: Ensine-o a dominar ferramentas e automatizar tarefas. "
    "2. Carreira e Riqueza: Dê conselhos estratégicos e planos de ação. "
    "3. Concursos (CNU): Continue sendo o mestre nos estudos. "
    "4. Estilo de Vida: Ajude na organização e produtividade diária. "
    "Use linguagem ninja: direta, motivadora e estruturada em tópicos."
)

# Inicializa o modelo com as novas instruções
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", # Ou o 2.5/3 que você preferir
    system_instruction=system_prompt
)

st.title("🥷 NinjaBrain: Seu Mentor 360º")
st.caption("Especialista em Vida, IA e Concursos")

# Histórico de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de Chat
if prompt := st.chat_input("Em que vamos evoluir hoje, Kadson?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta do Ninja
    with st.chat_message("assistant"):
        # Envia o histórico para ele ter memória
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})