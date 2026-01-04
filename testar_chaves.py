import os
from dotenv import load_dotenv

# Carrega .env
load_dotenv()

# Remove BOM UTF-8
for key in list(os.environ.keys()):
    if key.startswith('\ufeff'):
        new_key = key.replace('\ufeff', '')
        os.environ[new_key] = os.environ[key]
        del os.environ[key]

# Lista de chaves para verificar
chaves = {
    'ANTHROPIC_API_KEY': 'Anthropic (Claude)',
    'OPENAI_API_KEY': 'OpenAI (GPT)',
    'GEMINI_API_KEY': 'Gemini',
    'PERPLEXITY_API_KEY': 'Perplexity'
}

print("=" * 60)
print("VERIFICACAO DE CHAVES API")
print("=" * 60)
print()

todas_ok = True

for chave, nome in chaves.items():
    valor = os.getenv(chave)
    if valor:
        # Mostra apenas os primeiros e últimos caracteres por segurança
        inicio = valor[:10]
        fim = valor[-5:] if len(valor) > 15 else "***"
        print(f"OK: {nome}: ENCONTRADA")
        print(f"   Chave: {inicio}...{fim}")
    else:
        print(f"ERRO: {nome}: NAO ENCONTRADA")
        todas_ok = False
    print()

print("=" * 60)
if todas_ok:
    print("SUCESSO: TODAS AS CHAVES ESTAO CONFIGURADAS!")
    print()
    print("Proximos passos:")
    print("1. Instale as dependencias: pip install -r requirements.txt")
    print("2. Execute o app: streamlit run app.py")
else:
    print("ATENCAO: Algumas chaves estao faltando.")
    print("   Adicione as chaves faltantes no arquivo .env")
print("=" * 60)

