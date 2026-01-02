import streamlit as st
import google.generativeai as genai

# 1. Configuração de Layout e Tema
st.set_page_config(page_title="NinjaBrain OS", layout="wide", initial_sidebar_state="expanded")

# Estilo para botões e interface
st.markdown("""
<style>
    .stDownloadButton, .stButton { width: 100%; }
</style>
""", unsafe_allow_html=True)

# 2. Conexão Segura com a API
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Erro: Configure a GEMINI_API_KEY nos Secrets do Streamlit Cloud.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Personalidade e Modelo
# Usando gemini-1.5-flash sem prefixos beta para estabilidade
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. BARRA LATERAL (Ferramentas e Exportação)
with st.sidebar:
    st.title("🧰 Ferramentas")
    modo = st.radio("Escolha o Foco:", ["🧠 Mentor de Vida", "🛠️ Arquiteto de PRD"])
    
    st.divider()
    st.subheader("📁 Central de Arquivos")
    arquivo = st.file_uploader("Subir PDF, Imagem ou Áudio", type=['pdf', 'png', 'jpg', 'mp3', 'wav'])
    
    st.divider()
    st.subheader("📤 Exportar Resposta")
    # Espaço reservado para os botões que aparecerão após a resposta

# 5. INTERFACE DE CHAT
st.title(f"🚀 NinjaBrain: {modo}")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Entrada de texto
if prompt := st.chat_input("Em que vamos evoluir hoje, Kadson?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Ajuste de instrução conforme o modo
            contexto = "Atue como Mentor de Vida." if modo == "🧠 Mentor de Vida" else "Atue como Arquiteto de PRD Profissional."
            prompt_final = f"{contexto} {prompt}"
            
            # Chamada multimodal ou simples
            if arquivo:
                res = model.generate_content([prompt_final, arquivo])
            else:
                res = model.generate_content(prompt_final)
            
            texto_final = res.text
            st.markdown(texto_final)
            st.session_state.messages.append({"role": "assistant", "content": texto_final})
            
            # --- ATUALIZAÇÃO DOS BOTÕES NA BARRA LATERAL ---
            with st.sidebar:
                st.download_button("📥 Baixar como TXT", texto_final, file_name="ninja_brain.txt")
                # Gerando um .doc simples via texto
                st.download_button("📄 Exportar para Word", texto_final, file_name="ninja_brain.doc")
                st.info("Para imprimir: Pressione Ctrl + P")
                
        except Exception as e:
            st.error(f"Ocorreu um erro técnico. Verifique se sua chave API é nova e exclusiva.")
            st.info("Dica: Se o erro 404 persistir, dê um 'Reboot app' nas configurações do Streamlit.")