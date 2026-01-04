# 🚀 Como Fazer Deploy do Chat com IA

## ⚡ Guia Rápido (5 minutos)

### **1. Instalar Vercel CLI**
```bash
npm install -g vercel
```

### **2. Fazer Login**
```bash
vercel login
```

### **3. Deploy**
```bash
vercel
```

Siga as instruções:
- **Link to existing project?** → N (primeira vez)
- **Project name?** → `ninjabrain` (ou o nome que preferir)
- **Directory?** → `.` (raiz do projeto)

### **4. Configurar Variável de Ambiente**

Após o primeiro deploy, você receberá uma URL. Agora configure a chave da API:

1. Acesse: https://vercel.com/dashboard
2. Selecione seu projeto
3. Vá em **Settings** → **Environment Variables**
4. Adicione:
   - **Key:** `GEMINI_API_KEY`
   - **Value:** Sua chave da Gemini (obter em: https://aistudio.google.com/apikey)
   - **Environment:** Marque todas (Production, Preview, Development)
5. Clique em **Save**

### **5. Atualizar URL no Código**

1. Copie a URL do seu projeto (ex: `https://ninjabrain-abc123.vercel.app`)
2. Abra `app/app.js`
3. Encontre a linha:
   ```javascript
   const API_CHAT_URL = 'https://SEU-PROJETO.vercel.app/api/chat';
   ```
4. Substitua por sua URL:
   ```javascript
   const API_CHAT_URL = 'https://ninjabrain-abc123.vercel.app/api/chat';
   ```
5. Salve e faça commit:
   ```bash
   git add app/app.js
   git commit -m "Atualizar URL da API de chat"
   git push
   ```

### **6. Redeploy (se necessário)**

Se você já fez deploy antes de configurar a variável:
```bash
vercel --prod
```

Ou simplesmente faça um novo commit e o Vercel fará deploy automático.

---

## ✅ Verificar se Funcionou

1. Acesse seu web app: https://kpedro.github.io/NinjaBrain/
2. Clique no botão 💬 (canto inferior direito)
3. Digite uma pergunta (ex: "Como estudar matemática?")
4. Veja a resposta da IA!

---

## 🐛 Problemas Comuns

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

- [ ] Vercel CLI instalado
- [ ] Login feito no Vercel
- [ ] Deploy realizado
- [ ] Variável `GEMINI_API_KEY` configurada
- [ ] URL atualizada no `app/app.js`
- [ ] Testado no web app

---

**Pronto! Seu chat com IA está no ar! 🎉**

