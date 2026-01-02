import os

import requests
from dotenv import load_dotenv

# 1. Carrega sua chave do .env
load_dotenv()
api_key = os.getenv("PERPLEXITY_API_KEY")

print("--- 🥷 NinjaBrain: Ativando Pesquisa Real-Time ---")

if not api_key:
    print("❌ ERRO: Sua PERPLEXITY_API_KEY não foi encontrada no .env!")
else:
    # 2. Configura a busca na Perplexity
    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "sonar-reasoning",
        "messages": [{"role": "user", "content": "Quais as matérias do Bloco 8 do CNU?"}]
    }

    try:
        print("Buscando informações na Web... 🧠")
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        print("\n✅ RESPOSTA DA PERPLEXITY:")
        print(data['choices'][0]['message']['content'])
    except Exception as e:
        print(f"❌ Ocorreu um erro técnico: {e}")

print("\n--- 🏁 Operação Finalizada ---")