import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Configuração de ambiente
load_dotenv()
chave = os.getenv("GEMINI_API_KEY")

if not chave:
    print("❌ Erro: Verifique sua chave no arquivo .env")
else:
    genai.configure(api_key=chave)
    
    # 2. Escolhemos o modelo de elite que apareceu na sua lista
    model = genai.GenerativeModel('models/gemini-2.5-flash')
    
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