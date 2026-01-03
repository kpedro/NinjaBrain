import streamlit as st
import requests
import json

# 1. Configuração de Layout
st.set_page_config(page_title="NinjaBrain OS", layout="wide", initial_sidebar_state="expanded")

# 2. Configurações da API (Blindagem contra erro 404)
if "GEMINI_API_KEY" not in st.secrets:
    st.error("❌ Configure a GEMINI_API_KEY nos Secrets do Streamlit.")
    st.stop()

API_KEY = st.secrets["GEMINI_API_KEY"]
# URL FORÇADA PARA V1 (IGNORA O V1BETA PROBLEMÁTICO)
URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# 3. BARRA LATERAL (Botões e Ferramentas)
with st.sidebar:
    st.title("🧰 Ferramentas Ninja")
    st.success("🎯 Modo: Mentor de Vida")
    st.divider()
    st.subheader("📥 Exportar Mentoria")

# 4. INTERFACE DE CHAT
st.title("🚀 NinjaBrain OS: Conexão Estável")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Diga 'oi' para testar o túnel..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Construindo a requisição manual
            payload = {
                "contents": [{"parts": [{"text": "Atue como Mentor de Vida: " + prompt}]}]
            }
            headers = {'Content-Type': 'application/json'}
            
            # Realizando a chamada de rede direta
            response = requests.post(URL, headers=headers, data=json.dumps(payload))
            res_json = response.json()

            if response.status_code == 200:
                texto_resposta = res_json['candidates'][0]['content']['parts'][0]['text']
                st.markdown(texto_resposta)
                st.session_state.messages.append({"role": "assistant", "content": texto_resposta})
                
                # --- BOTÕES DE EXPORTAÇÃO NA SIDEBAR ---
                with st.sidebar:
                    st.download_button("📥 Baixar em TXT", texto_resposta, file_name="ninja_mentoria.txt")
                    st.download_button("📄 Salvar para Word", texto_resposta, file_name="ninja_mentoria.doc")
            else:
                st.error(f"Erro do Google: {res_json.get('error', {}).get('message', 'Erro desconhecido')}")
                st.info("Se o erro 404 persistir aqui, sua chave de API precisa ser recriada no Google AI Studio.")

        except Exception as e:
            st.error(f"Erro de Conexão: {e}")