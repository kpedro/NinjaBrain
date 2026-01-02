import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Configuração da Página
st.set_page_config(page_title="NinjaBrain - Segundo Cérebro", page_icon="🥷")
st.title("🥷 NinjaBrain: Seu Segundo Cérebro")

# 1. Carregar Chave do .env
load_dotenv()
chave = os.getenv("GEMINI_API_KEY")

if not chave:
    st.error("❌ Chave API não encontrada no arquivo .env")
else:
    genai.configure(api_key=chave)
    model = genai.GenerativeModel('models/gemini-2.5-flash')

    # Inicializar histórico do chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Exibir histórico de mensagens
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input do Usuário
    if prompt := st.chat_input("O que vamos estudar hoje, Kadson?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Resposta do NinjaBrain
        with st.chat_message("assistant"):
            with st.spinner("Ninja pensando... 🧠"):
                contexto = "Você é o NinjaBrain, focado no CNU 2026. Responda de forma direta com tabelas."
                response = model.generate_content(f"{contexto}\n\n{prompt}")
                full_response = response.text
                st.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})