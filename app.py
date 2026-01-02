import streamlit as st
import google.generativeai as genai

# 1. Configuração e Estética
st.set_page_config(page_title="NinjaBrain OS", layout="wide", initial_sidebar_state="expanded")

# 2. Conexão Segura
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Configure a GEMINI_API_KEY nos Secrets do Streamlit.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Inicialização do Modelo (Sem forçar versões beta)
# O modelo gemini-1.5-flash é o sucessor direto do que você conhecia como 2.5
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. BARRA LATERAL (Ferramentas e Botões)
with st.sidebar:
    st.title("🧰 Ferramentas Ninja")
    st.success("🎯 Modo: Mentor de Vida")
    
    st.divider()
    st.subheader("📁 Analisar Arquivos")
    arquivo = st.file_uploader("Subir PDF ou Imagem", type=['pdf', 'png', 'jpg', 'jpeg'])
    
    st.divider()
    st.subheader("📥 Exportar Mentoria")
    # Espaço para os botões aparecerem após a resposta

# 5. INTERFACE DE CHAT
st.title("🚀 NinjaBrain: Seu Mentor de Vida")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe histórico
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Como posso te ajudar hoje, Kadson?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Instrução de personalidade enviada diretamente no prompt
            prompt_mentoria = f"Atue como o NinjaBrain, um mentor de vida experiente. Responda ao Kadson: {prompt}"
            
            if arquivo:
                res = model.generate_content([prompt_mentoria, arquivo])
            else:
                res = model.generate_content(prompt_mentoria)
            
            texto_resposta = res.text
            st.markdown(texto_resposta)
            st.session_state.messages.append({"role": "assistant", "content": texto_resposta})
            
            # --- ATIVAÇÃO DOS BOTÕES DE EXPORTAÇÃO ---
            with st.sidebar:
                st.download_button("📥 Baixar TXT", texto_resposta, file_name="mentoria_ninja.txt")
                st.download_button("📄 Salvar Word (Doc)", texto_resposta, file_name="mentoria_ninja.doc")
                st.info("Dica: Use Ctrl+P para imprimir esta página.")
                
        except Exception as e:
            st.error(f"Erro de Conexão: {e}")
            st.info("Se o erro 404 persistir, tente dar REBOOT no app no painel do Streamlit.")