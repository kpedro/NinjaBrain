import streamlit as st
import google.generativeai as genai

# 1. Configuração de Alta Performance e Layout
st.set_page_config(
    page_title="NinjaBrain OS", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. Conexão com a API através dos Secrets do Streamlit
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("Erro ao carregar a chave API. Verifique os Secrets no Streamlit Cloud.")

# 3. Definição da Personalidade Híbrida
system_prompt = (
    "Você é o NinjaBrain OS, uma inteligência híbrida de alto nível. "
    "Sua missão é atuar em dois modos dependendo da necessidade do Kadson: "
    "MODO MENTOR: Ajuda em vida, finanças, estudos (CNU) e produtividade. "
    "MODO PRD ARCHITECT: Atua como um engenheiro de software sênior. Transforma ideias em "
    "Documentos de Requisitos (PRD) técnicos. Quando solicitado um app, você deve entregar: "
    "1. Objetivo; 2. Funcionalidades; 3. Tech Stack; 4. O Código pronto para o Cursor Free."
)

# 4. Inicialização do Modelo (Usando a versão mais estável para evitar erros)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)

# 5. Barra Lateral de Ferramentas
with st.sidebar:
    st.title("🥷 Ferramentas")
    modo = st.radio(
        "Escolha o Foco:", 
        ["🧠 Mentor de Vida", "🛠️ Arquiteto de PRD (Apps)"]
    )
    st.divider()
    upload = st.file_uploader(
        "Subir arquivo (PDF, Imagem, Áudio)", 
        type=['pdf', 'png', 'jpg', 'jpeg', 'mp3', 'wav']
    )
    if upload:
        st.success(f"Arquivo '{upload.name}' carregado!")

# 6. Interface Principal de Chat
st.title(f"🚀 NinjaBrain: {modo}")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibição do Histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 7. Lógica de Resposta e Processamento
if prompt := st.chat_input("O que vamos construir ou resolver hoje, Kadson?"):
    # Salva a pergunta do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Ajusta o prompt se estiver no modo PRD
            input_prompt = prompt
            if modo == "🛠️ Arquiteto de PRD (Apps)":
                input_prompt = f"Gere um PRD completo e o código inicial para esta ideia: {prompt}"
            
            # Processamento Multimodal (Texto + Arquivo se houver)
            if upload:
                response = model.generate_content([input_prompt, upload])
            else:
                response = model.generate_content(input_prompt)
                
            resposta_texto = response.text
            st.markdown(resposta_texto)
            
            # Salva a resposta do Ninja no histórico
            st.session_state.messages.append({"role": "assistant", "content": resposta_texto})
            
            # Botão de Exportação na barra lateral
            with st.sidebar:
                st.download_button(
                    label="📥 Baixar Resposta (TXT)",
                    data=resposta_texto,
                    file_name="ninja_output.txt",
                    mime="text/plain"
                )
        except Exception as e:
            st.error(f"Ocorreu um erro na geração: {e}")
            st.info("Dica: Verifique se sua chave API está ativa e se o modelo 'gemini-1.5-flash' está disponível.")