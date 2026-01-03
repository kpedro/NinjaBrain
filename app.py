import streamlit as st
import google.generativeai as genai

# 1. CONFIGURAÇÃO DE LAYOUT (Barra lateral sempre aberta)
st.set_page_config(
    page_title="NinjaBrain OS", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CONEXÃO BLINDADA (Configuração da Chave)
if "GEMINI_API_KEY" not in st.secrets:
    st.error("❌ ERRO: Adicione a GEMINI_API_KEY nos Secrets do Streamlit Cloud.")
    st.stop()

# O segredo do 'transport' resolve o erro 404 v1beta
genai.configure(api_key=st.secrets["GEMINI_API_KEY"], transport='rest')

# 3. INICIALIZAÇÃO DO MODELO
# Usando o flash que é o mais rápido e compatível
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. BARRA LATERAL (Ferramentas e Exportação)
with st.sidebar:
    st.title("🥷 Ferramentas Ninja")
    st.success("🎯 Modo: Mentor de Vida")
    
    st.divider()
    st.subheader("📁 Central de Arquivos")
    arquivo = st.file_uploader("Analisar PDF, Imagem ou Áudio", type=['pdf', 'png', 'jpg', 'jpeg', 'mp3', 'wav'])
    
    st.divider()
    st.subheader("📥 Exportar Mentoria")
    # Os botões aparecerão aqui dinamicamente abaixo

# 5. INTERFACE DE CHAT
st.title("🚀 NinjaBrain OS")

# Inicializa o histórico se não existir
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens do histórico
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# 6. LÓGICA DE PROCESSAMENTO
if prompt := st.chat_input("Como posso te ajudar hoje, Kadson?"):
    # Salva pergunta do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Instrução de personalidade embutida no prompt para evitar erro de sistema
            contexto = "Você é o NinjaBrain, mentor de vida focado em produtividade. "
            full_prompt = f"{contexto} Pergunta do Kadson: {prompt}"
            
            # Chamada Multimodal ou Simples
            if arquivo:
                res = model.generate_content([full_prompt, arquivo])
            else: