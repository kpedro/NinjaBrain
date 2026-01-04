# 🚀 Deploy do NinjaBrain no Vercel - Passo a Passo

## 📋 Passo 1: Fazer Login no Vercel

Execute no terminal:
```bash
vercel login
```

Isso vai:
1. Abrir o navegador automaticamente
2. Pedir para você fazer login (GitHub, Email, etc.)
3. Autorizar o Vercel CLI

**Após fazer login, volte ao terminal!**

---

## 📋 Passo 2: Fazer Deploy

No diretório do projeto (`C:\Users\Kadson\NinjaBrain`), execute:
```bash
vercel
```

### **Perguntas que aparecerão:**

1. **Set up and deploy "C:\Users\Kadson\NinjaBrain"?** 
   → Digite: `Y` (Yes)

2. **Which scope do you want to deploy to?**
   → Escolha sua conta (provavelmente "Kadson")

3. **Link to existing project?**
   → Digite: `N` (No - é um projeto novo)

4. **What's your project's name?**
   → Digite: `ninjabrain` (ou pressione Enter para usar o padrão)

5. **In which directory is your code located?**
   → Digite: `./` (ponto e barra - significa raiz do projeto)

6. **Want to override the settings?**
   → Digite: `N` (No - usar configurações padrão)

### **O que vai acontecer:**
- Vercel vai fazer upload dos arquivos
- Vai fazer build (se necessário)
- Vai fazer deploy

### **Resultado esperado:**
Você verá algo como:
```
✅ Production: https://ninjabrain-abc123.vercel.app
```

**⚠️ ANOTE ESTA URL!** Você precisará dela no próximo passo.

---

## 📋 Passo 3: Configurar Chave da API

### **3.1. Obter Chave da Gemini**

1. Acesse: https://aistudio.google.com/apikey
2. Faça login com sua conta Google
3. Clique em **"Create API Key"**
4. Copie a chave (começa com `AIza...`)

### **3.2. Adicionar no Vercel**

1. Acesse: https://vercel.com/dashboard
2. Clique no projeto **"ninjabrain"** (que acabou de criar)
3. Vá em **Settings** (no topo)
4. Clique em **Environment Variables** (menu lateral esquerdo)
5. Clique em **Add New**
6. Preencha:
   - **Key:** `GEMINI_API_KEY`
   - **Value:** Cole a chave que copiou
   - **Environment:** Marque todas as opções:
     - ☑ Production
     - ☑ Preview  
     - ☑ Development
7. Clique em **Save**

---

## 📋 Passo 4: Atualizar URL no Código

1. Abra o arquivo: `app/app.js`
2. Encontre a linha 298:
   ```javascript
   const API_CHAT_URL = 'https://SEU-PROJETO.vercel.app/api/chat';
   ```
3. Substitua pela URL do seu projeto (a que você anotou):
   ```javascript
   const API_CHAT_URL = 'https://ninjabrain-abc123.vercel.app/api/chat';
   ```
4. Salve o arquivo (Ctrl+S)

---

## 📋 Passo 5: Fazer Commit e Push

Execute no terminal:
```bash
git add app/app.js
git commit -m "feat: atualizar URL da API de chat para produção"
git push origin main
```

---

## 📋 Passo 6: Redeploy (se necessário)

Se você já fez deploy antes de configurar a variável de ambiente, faça um redeploy:

```bash
vercel --prod
```

Ou simplesmente aguarde o deploy automático após o push (se o GitHub estiver conectado).

---

## ✅ Verificar se Funcionou

1. Acesse: https://kpedro.github.io/NinjaBrain/
2. Clique no botão 💬 (canto inferior direito)
3. Digite uma pergunta (ex: "Como estudar matemática?")
4. Veja a resposta da IA!

---

## 🐛 Problemas Comuns

### **"No existing credentials found"**
- Execute: `vercel login`
- Faça login no navegador que abrir

### **"API key não configurada"**
- Verifique se `GEMINI_API_KEY` está no Vercel
- Certifique-se de que fez redeploy após adicionar

### **"CORS error"**
- O `vercel.json` já está configurado
- Verifique se a URL está correta no `app.js`

### **Chat não aparece**
- Abra o console (F12) e veja erros
- Verifique se a URL da API está correta

---

## 📝 Checklist

- [ ] Login feito (`vercel login`)
- [ ] Deploy realizado (`vercel`)
- [ ] URL anotada
- [ ] Chave Gemini obtida
- [ ] Variável `GEMINI_API_KEY` configurada no Vercel
- [ ] URL atualizada no `app/app.js`
- [ ] Commit e push feitos
- [ ] Testado no web app

---

**Boa sorte! 🚀**

