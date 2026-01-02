# Guia de Teste - NinjaBrain

## Pré-requisitos

1. **Python instalado** (versão 3.8 ou superior)
2. **Dependências instaladas**:
   ```bash
   python -m pip install -r requirements.txt
   ```
   Ou instale manualmente:
   ```bash
   python -m pip install requests python-dotenv google-generativeai
   ```

3. **Arquivo .env configurado** na raiz do projeto com:
   ```
   GEMINI_API_KEY=sua_chave_gemini_aqui
   PERPLEXITY_API_KEY=sua_chave_perplexity_aqui
   ```

## Como Testar

### 1. Testar o Brain (Gemini)

Execute o script do cérebro principal:

```bash
python backend/brain.py
```

**Resultado esperado:**
- ✅ Se a chave estiver correta: conexão com Gemini e resposta do assistente
- ❌ Se a chave estiver faltando: mensagem de erro indicando que GEMINI_API_KEY não foi encontrada

### 2. Testar o Search (Perplexity)

Execute o script de busca:

```bash
python backend/integrations/search.py
```

**Resultado esperado:**
- ✅ Se a chave estiver correta: busca sobre "Matérias do Bloco 8 do CNU" e exibe a resposta
- ❌ Se a chave estiver faltando: mensagem de erro indicando que PERPLEXITY_API_KEY não foi encontrada

## Verificações

### Verificar se o .env está correto:

1. O arquivo deve estar em: `C:\Users\Kadson\NinjaBrain\.env`
2. Formato do arquivo:
   ```
   GEMINI_API_KEY=AIza...
   PERPLEXITY_API_KEY=pplx-...
   ```
3. **IMPORTANTE**: Não use espaços ao redor do `=`
4. **IMPORTANTE**: Não use aspas nas chaves (a menos que façam parte da chave)

### Verificar dependências:

```bash
python -m pip list
```

Deve mostrar:
- requests
- python-dotenv
- google-generativeai (ou google-genai)

## Troubleshooting

### Erro: "PERPLEXITY_API_KEY não foi encontrada"
- Verifique se o arquivo `.env` está na raiz do projeto
- Verifique se a linha está escrita exatamente: `PERPLEXITY_API_KEY=...`
- Verifique se não há espaços extras
- Verifique se o arquivo está salvo (não apenas aberto no editor)

### Erro: "ModuleNotFoundError: No module named 'requests'"
- Instale as dependências: `python -m pip install -r requirements.txt`

### Erro: "UnicodeEncodeError"
- Já foi corrigido nos scripts, mas se aparecer, verifique o encoding do terminal

### Erro: "HTTP 401" ou "Unauthorized"
- A chave da API está incorreta ou expirada
- Verifique se copiou a chave completa
- Gere uma nova chave se necessário

## Teste Completo

Para testar tudo de uma vez:

```bash
# Teste 1: Brain
python backend/brain.py

# Teste 2: Search
python backend/integrations/search.py
```

Ambos devem funcionar se as chaves estiverem corretas no `.env`!


