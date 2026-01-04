import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Localiza o arquivo .env na pasta raiz
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(base_dir, '.env')

# 2. Carrega as variáveis
load_dotenv(dotenv_path)

# Remove BOM de todas as variáveis de ambiente (corrige problema de encoding UTF-8 com BOM)
for key in list(os.environ.keys()):
    if key.startswith('\ufeff'):
        new_key = key.replace('\ufeff', '')
        os.environ[new_key] = os.environ[key]
        del os.environ[key]

chave = os.getenv("GEMINI_API_KEY")

if not chave:
    print("❌ Erro: Verifique sua chave no arquivo .env")
else:
    genai.configure(api_key=chave)
    
    # 2. Usa modelo disponível (tenta 2.0-flash primeiro, fallback para pro)
    try:
        model = genai.GenerativeModel('models/gemini-2.0-flash')
    except:
        try:
            model = genai.GenerativeModel('models/gemini-pro')
        except:
            model = genai.GenerativeModel('gemini-pro')
    
    # 3. Personalidade do Agente
    contexto = """
    Você é o NinjaBrain, assistente pessoal do Kadson para o CNU 2026.
    Sua missão é ser direto, técnico e focado em aprovação. 
    Sempre que possível, use tabelas para organizar as informações.
    """

    print("--- 🥷 NinjaBrain Online (Gemini 2.5) ---")
    
    while True:
        pergunta = input("\nKadson (ou 'sair'): ")
        if pergunta.lower() == 'sair':
            break
            
        print("Ninja pensando... 🧠")
        
        try:
            # Enviamos o contexto de Ninja junto com a pergunta
            response = model.generate_content(f"{contexto}\n\nPergunta: {pergunta}")
            print(f"\n🤖 NINJABRAIN:\n{response.text}")
        except Exception as e:
            print(f"❌ Erro na resposta: {e}")