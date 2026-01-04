import os
import requests
from dotenv import load_dotenv

# 1. Localiza o arquivo .env na pasta raiz
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
dotenv_path = os.path.join(base_dir, '.env')

# 2. Carrega sua chave do .env
load_dotenv(dotenv_path)

# Remove BOM de todas as variáveis de ambiente (corrige problema de encoding UTF-8 com BOM)
for key in list(os.environ.keys()):
    if key.startswith('\ufeff'):
        new_key = key.replace('\ufeff', '')
        os.environ[new_key] = os.environ[key]
        del os.environ[key]

api_key = os.getenv("PERPLEXITY_API_KEY")

print("--- 🥷 NinjaBrain: Ativando Pesquisa Real-Time ---")

if not api_key:
    print("❌ ERRO: Sua PERPLEXITY_API_KEY não foi encontrada no .env!")
else:
    # 2. Configura a busca na Perplexity
    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "sonar",  # Modelo atualizado (sonar-reasoning foi descontinuado)
        "messages": [{"role": "user", "content": "Quais as matérias do Bloco 8 do CNU?"}]
    }

    try:
        print("Buscando informações na Web... 🧠")
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Levanta exceção se status code não for 2xx
        
        data = response.json()
        
        # Verifica se a resposta tem a estrutura esperada
        if 'choices' in data and len(data['choices']) > 0:
            print("\n✅ RESPOSTA DA PERPLEXITY:")
            print(data['choices'][0]['message']['content'])
        else:
            print("❌ Resposta da API em formato inesperado:")
            print(data)
            
    except requests.exceptions.HTTPError as e:
        print(f"❌ Erro HTTP: {e}")
        if hasattr(e.response, 'text'):
            print(f"Detalhes: {e.response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
    except KeyError as e:
        print(f"❌ Erro ao processar resposta: campo {e} não encontrado")
    except Exception as e:
        print(f"❌ Ocorreu um erro técnico: {e}")

print("\n--- 🏁 Operação Finalizada ---")