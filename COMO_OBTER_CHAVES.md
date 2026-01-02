# Como Obter as Chaves de API

## Resumo

Você precisa de **2 chaves**:
1. **GEMINI_API_KEY** - Para o assistente principal (brain.py)
2. **PERPLEXITY_API_KEY** - Para buscas na web (search.py)

---

## 1. Chave do Gemini (Google AI)

### Status Atual
- ✅ Chave encontrada no .env
- ❌ Chave inválida (erro 400: API key not valid)

### Como Obter/Verificar:

1. **Acesse**: https://aistudio.google.com/apikey
2. **Faça login** com sua conta Google
3. **Crie uma nova chave** ou **copie uma existente**
   - Clique em "Create API Key"
   - Escolha o projeto (ou crie um novo)
   - Copie a chave (começa com `AIza...`)
4. **Atualize no .env**:
   ```
   GEMINI_API_KEY=AIzaSyC... (cole a chave completa aqui)
   ```

### Nota Importante:
- A chave atual no seu .env está inválida ou expirada
- Você pode usar a mesma chave se ela ainda estiver válida
- Ou criar uma nova chave no link acima

---

## 2. Chave da Perplexity

### Status Atual
- ❌ Chave não encontrada no .env

### Como Obter:

1. **Acesse**: https://www.perplexity.ai/
2. **Faça login** ou crie uma conta
3. **Vá para**: https://www.perplexity.ai/settings/api
   - Ou procure por "API" nas configurações
4. **Gere uma nova chave API**
   - Clique em "Generate API Key" ou similar
   - Copie a chave (começa com `pplx-...`)
5. **Adicione no .env**:
   ```
   PERPLEXITY_API_KEY=pplx-... (cole a chave completa aqui)
   ```

### Alternativa (se não encontrar):
- Acesse diretamente: https://www.perplexity.ai/settings/api
- Ou procure no menu de configurações da sua conta

---

## Formato Final do Arquivo .env

Seu arquivo `.env` deve ficar assim (na raiz do projeto):

```
GEMINI_API_KEY=AIzaSyC_sua_chave_gemini_completa_aqui
PERPLEXITY_API_KEY=pplx_sua_chave_perplexity_completa_aqui
```

### ⚠️ IMPORTANTE:
- **Sem espaços** antes ou depois do `=`
- **Sem aspas** ao redor das chaves
- **Uma chave por linha**
- **Sem linhas em branco** entre as chaves (opcional, mas melhor evitar)

---

## Verificação Rápida

Após adicionar/atualizar as chaves:

```bash
# Teste 1: Verifica se o Gemini funciona
python backend/brain.py

# Teste 2: Verifica se o Perplexity funciona
python backend/integrations/search.py
```

### Resultados Esperados:

✅ **Sucesso no Gemini:**
```
OK: Chave encontrada! Conectando ao Gemini...
Pensando...
RESPOSTA DO GEMINI:
------------------------------
[Resposta do assistente]
------------------------------
SISTEMA ONLINE!
```

✅ **Sucesso no Perplexity:**
```
--- NinjaBrain: Ativando Pesquisa Real-Time ---
Buscando informacoes na Web...
RESPOSTA DA PERPLEXITY:
[Resposta sobre as matérias do Bloco 8 do CNU]
```

---

## Problemas Comuns

### "API key not valid" (Gemini)
- A chave está incorreta ou expirada
- **Solução**: Gere uma nova chave em https://aistudio.google.com/apikey

### "PERPLEXITY_API_KEY não foi encontrada"
- A linha não está no arquivo .env
- **Solução**: Adicione a linha `PERPLEXITY_API_KEY=pplx-...` no .env

### "HTTP 401" ou "Unauthorized"
- Chave inválida ou sem permissões
- **Solução**: Verifique se copiou a chave completa e se ela está ativa

---

## Dicas

1. **Mantenha as chaves seguras**: Nunca compartilhe ou commite o arquivo .env no Git
2. **Verifique limites**: Algumas APIs têm limites de uso gratuito
3. **Teste uma de cada vez**: Configure e teste o Gemini primeiro, depois o Perplexity


