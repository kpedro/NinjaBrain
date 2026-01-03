import streamlit as st
import google.generativeai as genai

# 1. Configuração de Layout
st.set_page_config(page_title="NinjaBrain OS", layout="wide", initial_sidebar_state="expanded")

# 2. Conexão Estável
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Configure a GEMINI_API_KEY nos Secrets.")
    st.stop()

# Configuração simples e direta
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Inicialização do Modelo (Mudando para o modelo PRO estável)
# O Gemini Pro é o mais compatível com chaves de API padrão
model = genai.GenerativeModel('gemini-pro')

# 4. Barra Lateral
with st.sidebar:
    st.title("🧰 Ferramentas Ninja")
    st.success("🎯 Modo: Mentor de Vida")
    st.divider()
    # No gemini-pro simples, o upload de arquivos funciona de forma diferente, 
    # então vamos focar primeiro em fazer o texto funcionar.
    st.subheader("📥 Exportar Mentoria")

# 5. Interface de Chat
st.title("🚀 NinjaBrain OS")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Diga algo para testar o Ninja..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Chamada de geração de conteúdo
            res = model.generate_content(prompt)
            resposta = res.text
            
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})
            
            # --- BOTÕES DE EXPORTAÇÃO (Sempre visíveis após resposta) ---
            with st.sidebar:
                st.download_button("📥 Baixar TXT", resposta, file_name="ninja.txt")
                st.download_button("📄 Salvar Word", resposta, file_name="ninja.doc")
                
        except Exception as e:
            st.error(f"Erro Crítico: {e}")
            st.info("💡 Kadson, se este erro 404 persistir com o gemini-pro, o problema está na sua chave. Tente criar uma nova chave especificamente em um 'Novo Projeto' no Google AI Studio.")