# 🚀 Deploy do Chat com IA - Passo a Passo

## ✅ Status Atual
- ✅ Dependências instaladas (`npm install`)
- ⏳ Próximo: Deploy no Vercel

---

## 📋 Passo a Passo

### **1. Instalar Vercel CLI (se ainda não tiver)**

```bash
npm install -g vercel
```

### **2. Fazer Login no Vercel**

```bash
vercel login
```

Isso abrirá o navegador para você fazer login com GitHub/Email.

### **3. Fazer Deploy**

No diretório do projeto:
```bash
vercel
```

**Perguntas que aparecerão:**
- **Set up and deploy?** → `Y` (Yes)
- **Which scope?** → Escolha sua conta
- **Link to existing project?** → `N` (primeira vez)
- **What's your project's name?** → `ninjabrain` (ou o nome que preferir)
- **In which directory is your code located?** → `./` (ponto, significa raiz)

### **4. Anotar a URL**

Após o deploy, você verá algo como:
```
✅ Production: https://ninjabrain-abc123.vercel.app
```

**ANOTE ESTA URL!** Você precisará dela no próximo passo.

### **5. Configurar Variável de Ambiente**

1. Acesse: https://vercel.com/dashboard
2. Clique no seu projeto (`ninjabrain`)
3. Vá em **Settings** (no topo)
4. Clique em **Environment Variables** (menu lateral)
5. Clique em **Add New**
6. Preencha:
   - **Key:** `GEMINI_API_KEY`
   - **Value:** Sua chave da Gemini (veja como obter abaixo)
   - **Environment:** Marque todas (Production, Preview, Development)
7. Clique em **Save**

**Como obter chave Gemini:**
1. Acesse: https://aistudio.google.com/apikey
2. Clique em **Create API Key**
3. Copie a chave (começa com `AIza...`)

### **6. Atualizar URL no Código**

1. Abra `app/app.js`
2. Encontre a linha (por volta da linha 290):
   ```javascript
   const API_CHAT_URL = 'https://SEU-PROJETO.vercel.app/api/chat';
   ```
3. Substitua pela URL do seu projeto:
   ```javascript
   const API_CHAT_URL = 'https://ninjabrain-abc123.vercel.app/api/chat';
   ```
4. Salve o arquivo

### **7. Fazer Commit e Push**

```bash
git add app/app.js
git commit -m "feat: atualizar URL da API de chat"
git push origin main
```

### **8. Redeploy (se necessário)**

Se você já fez deploy antes de configurar a variável de ambiente:
```bash
vercel --prod
```

Ou simplesmente aguarde o deploy automático após o push.

---

## ✅ Verificar se Funcionou

1. Acesse seu web app: https://kpedro.github.io/NinjaBrain/
2. Clique no botão 💬 (canto inferior direito)
3. Digite uma pergunta (ex: "Como estudar matemática?")
4. Veja a resposta da IA!

---

## 🐛 Problemas?

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

## 📝 Checklist Final

- [ ] Vercel CLI instalado
- [ ] Login feito (`vercel login`)
- [ ] Deploy realizado (`vercel`)
- [ ] URL anotada
- [ ] Variável `GEMINI_API_KEY` configurada no Vercel
- [ ] URL atualizada no `app/app.js`
- [ ] Commit e push feitos
- [ ] Testado no web app

---

**Boa sorte com o deploy! 🚀**

