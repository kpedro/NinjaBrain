# 👁️ Como Ver Prévia no Cursor

## 🎯 Métodos para Ver Prévia

### **Método 1: Preview HTML (Recomendado no Cursor)**

1. **Abra o arquivo HTML:**
   - Navegue até `app/index.html`
   - Clique com botão direito no arquivo

2. **Opções de Preview:**
   - **Opção A:** Clique direito → "Open Preview" ou "Show Preview"
   - **Opção B:** Use o atalho `Ctrl+Shift+V` (ou `Cmd+Shift+V` no Mac)
   - **Opção C:** Procure pelo ícone de "preview" na barra superior

3. **Se não aparecer:**
   - O Cursor pode não ter preview nativo para HTML
   - Use o Método 2 ou 3 abaixo

---

### **Método 2: Abrir no Navegador (Mais Confiável)**

1. **Clique direito em `app/index.html`**
2. **Selecione:** "Open with..." ou "Reveal in File Explorer"
3. **Abra o arquivo no navegador:**
   - Arraste o arquivo para o navegador
   - Ou clique duas vezes (se o navegador for padrão para HTML)

**⚠️ Nota:** Este método pode não carregar o markdown corretamente (problema de CORS)

---

### **Método 3: Servidor Local (Melhor Opção)**

1. **Abra o terminal no Cursor:**
   - `Ctrl+`` (backtick) ou Terminal → New Terminal

2. **Execute:**
   ```powershell
   cd app
   python -m http.server 8000
   ```

3. **Abra no navegador:**
   - Pressione `Ctrl+Click` em `http://localhost:8000`
   - Ou digite manualmente no navegador

**✅ Vantagem:** Funciona perfeitamente, carrega todos os recursos

---

### **Método 4: Extensão Live Server (Se Disponível)**

1. **Instale extensão "Live Server"** (se o Cursor suportar)
2. **Clique direito em `index.html`**
3. **Selecione "Open with Live Server"**

---

## 🎯 Recomendação

**Use o Método 3 (Servidor Local)** porque:
- ✅ Carrega todos os recursos corretamente
- ✅ Markdown funciona (sem CORS)
- ✅ JavaScript funciona perfeitamente
- ✅ Simula ambiente real

---

## 🚀 Atalho Rápido

**No terminal do Cursor:**
```powershell
cd app; python -m http.server 8000
```

Depois abra: **http://localhost:8000**

---

## 💡 Dica

Se quiser que o Cursor abra automaticamente:
1. Execute o servidor
2. Use `Ctrl+Click` no link `http://localhost:8000` no terminal
3. Ou configure um atalho personalizado

---

**O servidor já está rodando em background! Acesse: http://localhost:8000** 🚀

