# 🔐 Como Configurar o Arquivo .env

## 📍 Localização

O arquivo `.env` deve estar na **raiz do projeto**:
```
C:\Users\Kadson\NinjaBrain\.env
```

---

## ✏️ Formato do Arquivo

Abra o arquivo `.env` em um editor de texto (Notepad++, VS Code, etc.) e adicione as chaves assim:

### **Opção 1: Anthropic (Claude) - RECOMENDADO**

```env
ANTHROPIC_API_KEY=sk-ant-api03-sua_chave_completa_aqui
```

### **Opção 2: OpenAI (GPT)**

```env
OPENAI_API_KEY=sk-proj-sua_chave_completa_aqui
```

### **Opção 3: Ambos (com fallback automático)**

```env
ANTHROPIC_API_KEY=sk-ant-api03-sua_chave_anthropic_aqui
OPENAI_API_KEY=sk-proj-sua_chave_openai_aqui
```

---

## ⚠️ REGRAS IMPORTANTES

### ✅ **FAÇA:**
- Sem espaços antes ou depois do `=`
- Sem aspas ao redor da chave
- Uma chave por linha
- Salve o arquivo após editar

### ❌ **NÃO FAÇA:**
- `ANTHROPIC_API_KEY = "sua_chave"` ❌ (espaços e aspas)
- `ANTHROPIC_API_KEY=sua_chave` ✅ (correto)

---

## 🔑 Como Obter as Chaves

### **Anthropic (Claude):**

1. Acesse: https://console.anthropic.com/
2. Faça login ou crie conta
3. Vá em **API Keys**
4. Clique em **Create Key**
5. Copie a chave (começa com `sk-ant-api03-...`)

### **OpenAI (GPT):**

1. Acesse: https://platform.openai.com/api-keys
2. Faça login
3. Clique em **Create new secret key**
4. Copie a chave (começa com `sk-proj-...`)

---

## 📝 Exemplo Completo do Arquivo .env

```env
# API para o app.py (Mentor de Vida)
ANTHROPIC_API_KEY=sk-ant-api03-abc123def456...

# API para buscas (opcional)
PERPLEXITY_API_KEY=pplx-abc123def456...

# API Gemini (para scripts backend, opcional)
GEMINI_API_KEY=AIzaSyC-abc123def456...
```

---

## ✅ Verificar se Funcionou

Após salvar o `.env`, teste:

```bash
# Testar app.py
streamlit run app.py
```

Se aparecer "✅ Conectado via: ANTHROPIC" ou "OPENAI", está funcionando!

---

## 🛡️ Segurança

- ✅ O arquivo `.env` está no `.gitignore` (não vai para o GitHub)
- ✅ Nunca compartilhe suas chaves
- ✅ Não commite o `.env` no Git

---

## 🆘 Problemas Comuns

### "Chave não encontrada"
- Verifique se o arquivo está na raiz do projeto
- Verifique se não há espaços extras
- Verifique se salvou o arquivo

### "Erro 401/403"
- Chave inválida ou expirada
- Gere uma nova chave

### "Biblioteca não encontrada"
```bash
pip install anthropic
# OU
pip install openai
```

---

**Pronto! Configure e teste! 🚀**


