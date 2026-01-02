import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega sua chave do .env
load_dotenv()
chave = os.getenv("GEMINI_API_KEY")

if not chave:
    print("❌ Erro: Chave não encontrada no .env")
else:
    genai.configure(api_key=chave)
    print("--- 🔎 Listando Modelos Disponíveis para sua Chave ---")
    
    try:
        # Este comando pergunta ao Google quais nomes você deve usar
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ Use este nome: {m.name}")
    except Exception as e:
        print(f"❌ Erro ao listar: {e}")
