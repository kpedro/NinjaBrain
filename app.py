import streamlit as st
import google.generativeai as genai

# 1. CONFIGURAÇÃO DE LAYOUT
st.set_page_config(
    page_title="NinjaBrain OS", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CONEXÃO COM A API (Secrets)
if "GEMINI_API_KEY" not in st.secrets:
    st.error("❌ ERRO: Adicione a GEMINI_API_KEY nos Secrets do Streamlit Cloud.")
    st.stop()

# Configuração com transporte REST para evitar erro 404 v1beta
genai.configure(api_key=st.secrets["GEMINI_API_KEY"], transport='rest')

# 3. INICIALIZAÇÃO DO MODELO
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

# 5. INTERFACE DE CHAT
st.title("🚀 NinjaBrain OS")

# Inicializa o histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# 6. LÓGICA DE PROCESSAMENTO (Indentação corrigida)
if prompt := st.chat_input("Como posso te ajudar hoje, Kadson?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Contexto de personalidade
            contexto = "Você é o NinjaBrain, mentor de vida focado em produtividade. "
            full_prompt = f"{contexto} Pergunta do Kadson: {prompt}"
            
            # Chamada Multimodal ou Simples com indentação correta
            if arquivo:
                res = model.generate_content([full_prompt, arquivo])
            else:
                res = model.generate_content(full_prompt)
            
            texto_resposta = res.text
            st.markdown(texto_resposta)
            st.session_state.messages.append({"role": "assistant", "content": texto_resposta})
            
            # BOTÕES DE EXPORTAÇÃO NA SIDEBAR
            with st.sidebar:
                st.download_button(
                    label="📥 Baixar em TXT",
                    data=texto_resposta,
                    file_name="mentoria_ninja.txt",
                    mime="text/plain"
                )
                st.download_button(
                    label="📄 Salvar para Word",
                    data=texto_resposta,
                    file_name="mentoria_ninja.doc",
                    mime="application/vnd.ms-word"
                )
                st.info("Para imprimir: Pressione Ctrl + P")

        except Exception as e:
            st.error(f"Erro na conexão: {e}")