import streamlit as st
import google.generativeai as genai

# 1. Configuração de Layout
st.set_page_config(page_title="NinjaBrain OS", layout="wide")

# 2. Conexão com a API (Sem firulas)
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Configure a GEMINI_API_KEY nos Secrets do Streamlit.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Inicialização do Modelo (Padrão de Fábrica)
# Removendo system_instruction para evitar o erro 404 de versão
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. Barra Lateral com Ferramentas
with st.sidebar:
    st.title("🥷 Ferramentas")
    st.info("Modo: Mentor de Vida Ativado")
    
    st.divider()
    st.subheader("📁 Arquivos")
    arquivo = st.file_uploader("Analisar PDF ou Imagem", type=['pdf', 'png', 'jpg', 'jpeg'])
    
    st.divider()
    st.subheader("📤 Exportar")
    # Os botões aparecerão aqui após a resposta

# 5. Interface de Chat
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
            # Envio simples para garantir conexão
            if arquivo:
                res = model.generate_content([prompt, arquivo])
            else:
                res = model.generate_content(prompt)
            
            resposta_texto = res.text
            st.markdown(resposta_texto)
            st.session_state.messages.append({"role": "assistant", "content": resposta_texto})
            
            # --- BOTÕES DE EXPORTAÇÃO ---
            with st.sidebar:
                st.download_button("📥 Baixar em TXT", resposta_texto, file_name="mentoria_ninja.txt")
                st.download_button("📄 Salvar para Word", resposta_texto, file_name="mentoria_ninja.doc")
                
        except Exception as e:
            st.error(f"Erro ao conectar com o cérebro da IA: {e}")
            st.info("Dica: Se o erro persistir, gere uma nova chave no Google AI Studio e dê REBOOT no app.")