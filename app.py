import streamlit as st
import google.generativeai as genai

# 1. Configuração de Layout e Tema
st.set_page_config(page_title="NinjaBrain OS", layout="wide", initial_sidebar_state="expanded")

# 2. Conexão com a API (Usando a nova chave que você gerou)
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Configure a GEMINI_API_KEY nos Secrets do Streamlit.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Personalidade do Ninja
system_prompt = (
    "Você é o NinjaBrain OS. "
    "MODO MENTOR: Foco em vida e carreira. "
    "MODO PRD: Foco em engenharia de software e criação de apps."
)

# 4. Inicialização do Modelo (Correção do Erro 404)
# Usamos o modelo sem prefixos beta para garantir estabilidade
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# 5. Barra Lateral (Ferramentas e Exportação)
with st.sidebar:
    st.title("🥷 Painel Ninja")
    modo = st.radio("Foco Atual:", ["🧠 Mentor de Vida", "🛠️ Arquiteto de PRD"])
    
    st.divider()
    st.subheader("📁 Arquivos e Mídia")
    upload = st.file_uploader("Analisar PDF, Imagem ou Áudio", type=['pdf', 'png', 'jpg', 'mp3'])
    
    st.divider()
    st.subheader("📤 Ações")
    # Os botões de download aparecem aqui após a conversa
    placeholder_export = st.empty()

# 6. Interface de Chat
st.title(f"🚀 NinjaBrain: {modo}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Como vamos evoluir hoje, Kadson?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Lógica de resposta
            input_data = [prompt]
            if upload:
                input_data.append(upload)
            
            response = model.generate_content(input_data)
            full_res = response.text
            st.markdown(full_res)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

            # Atualiza os botões de exportação na barra lateral
            with placeholder_export.container():
                st.download_button("📥 Baixar em TXT", full_res, file_name="ninja_brain.txt")
                st.download_button("📄 Exportar para Word (Doc)", full_res, file_name="ninja_brain.doc")
                st.info("💡 Para imprimir: Use Ctrl+P no seu navegador.")

        except Exception as e:
            st.error(f"Erro técnico: {e}")
            st.info("Dica: Se o erro 404 persistir, verifique se a sua chave API é nova e exclusiva.")