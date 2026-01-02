import streamlit as st
import google.generativeai as genai

# 1. Configuração de Layout
st.set_page_config(page_title="NinjaBrain OS", layout="wide", initial_sidebar_state="expanded")

# 2. Conexão com a API (Secrets)
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Configure a GEMINI_API_KEY nos Secrets do Streamlit.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Inicialização do Modelo (Usando o 1.5 Flash - o mais rápido do mundo)
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. BARRA LATERAL (Ferramentas e Botões)
with st.sidebar:
    st.title("🧰 Ferramentas Ninja")
    st.info("🎯 Modo: Mentor de Vida Ativado")
    
    st.divider()
    st.subheader("📁 Analisar Arquivos")
    arquivo = st.file_uploader("Subir PDF ou Imagem", type=['pdf', 'png', 'jpg', 'jpeg'])
    
    st.divider()
    st.subheader("📤 Exportar e Salvar")
    # Os botões aparecerão aqui após o Ninja responder

# 5. INTERFACE DE CHAT
st.title("🚀 NinjaBrain: Mentor de Vida")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Como posso te ajudar hoje, Kadson?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Comando de sistema direto no prompt para evitar erro de configuração
            instrucao = "Você é o NinjaBrain, um mentor de vida focado em produtividade e finanças. "
            prompt_completo = f"{instrucao} Pergunta: {prompt}"
            
            if arquivo:
                res = model.generate_content([prompt_completo, arquivo])
            else:
                res = model.generate_content(prompt_completo)
            
            texto_final = res.text
            st.markdown(texto_final)
            st.session_state.messages.append({"role": "assistant", "content": texto_final})
            
            # --- RECOLOCANDO OS BOTÕES DE EXPORTAÇÃO ---
            with st.sidebar:
                st.download_button("📥 Baixar em TXT", texto_final, file_name="ninja_brain.txt")
                st.download_button("📄 Salvar para Word (Doc)", texto_final, file_name="ninja_brain.doc")
                st.success("Pronto! Escolha como salvar acima.")
                
        except Exception as e:
            st.error(f"Erro técnico: {e}")
            st.warning("Dica: Se o erro 404 persistir, o problema está na CHAVE de API. Gere uma nova no Google AI Studio.")