# 🔧 Solução para Erro 404 no GitHub Pages

## ⚠️ Problema

Você está vendo "404 - There isn't a GitHub Pages site here."

Isso significa que o GitHub Pages **não está ativado** ou o **deploy não funcionou**.

---

## ✅ Solução Passo a Passo

### **PASSO 1: Ativar GitHub Pages (OBRIGATÓRIO)**

1. **Acesse este link:**
   ```
   https://github.com/kpedro/NinjaBrain/settings/pages
   ```

2. **Configure:**
   - **Source:** Selecione **"GitHub Actions"**
   - Clique em **"Save"**

3. **IMPORTANTE:** Se não aparecer a opção "GitHub Actions", use:
   - **Source:** "Deploy from a branch"
   - **Branch:** `main`
   - **Folder:** `/app`
   - Clique em **"Save"**

---

### **PASSO 2: Disparar o Workflow Manualmente**

1. **Acesse Actions:**
   ```
   https://github.com/kpedro/NinjaBrain/actions
   ```

2. **Clique em "Deploy to GitHub Pages"** (no menu lateral)

3. **Clique no botão "Run workflow"** (canto superior direito)

4. **Selecione branch:** `main`

5. **Clique em "Run workflow"**

6. **Aguarde 2-5 minutos**

---

### **PASSO 3: Verificar se Funcionou**

1. **Acesse Actions novamente:**
   ```
   https://github.com/kpedro/NinjaBrain/actions
   ```

2. **Clique no workflow que acabou de rodar**

3. **Verifique se todos os steps têm ✅ verde**

4. **Se algum step falhou, me avise qual erro apareceu**

---

### **PASSO 4: Acessar o Web App**

Depois que o workflow terminar com sucesso:

```
https://kpedro.github.io/NinjaBrain/
```

**Aguarde 1-2 minutos após o workflow terminar!**

---

## 🐛 Se Ainda Não Funcionar

### **Erro: "Workflow permissions"**

**Solução:**
1. Vá em **Settings > Actions > General**
2. Em **Workflow permissions**, selecione: **"Read and write permissions"**
3. Marque: **"Allow GitHub Actions to create and approve pull requests"**
4. Clique em **Save**

### **Erro: "Pages build failed"**

**Solução:**
1. Verifique se a pasta `app/` existe no repositório
2. Verifique se `app/index.html` existe
3. Veja os logs do workflow para identificar o erro

### **Ainda mostra 404 após 10 minutos**

**Soluções:**
1. Limpe o cache do navegador (Ctrl+Shift+Delete)
2. Tente em modo anônimo (Ctrl+Shift+N)
3. Verifique se o repositório é **público** (GitHub Pages gratuito só funciona em repositórios públicos)
4. Aguarde mais 5 minutos (primeira vez pode demorar até 15 minutos)

---

## 🔍 Verificar se Tudo Está Correto

### **Checklist:**

- [ ] Repositório é **público**? (Settings > General > Danger Zone > Change visibility)
- [ ] GitHub Pages está ativado? (Settings > Pages)
- [ ] Workflow rodou com sucesso? (Actions)
- [ ] Todos os arquivos estão no repositório? (`app/index.html`, `app/styles.css`, etc.)
- [ ] Aguardou pelo menos 5 minutos após ativar?

---

## 📞 Se Nada Funcionar

Me envie:
1. Screenshot da página Settings > Pages
2. Screenshot do workflow que rodou (Actions)
3. Qualquer mensagem de erro que apareceu

---

## ✅ Workflow Atualizado

Atualizei o workflow para usar versões mais recentes das actions. Faça um push:

```bash
cd C:\Users\Kadson\NinjaBrain
git add .github/workflows/deploy.yml
git commit -m "fix: atualiza workflow do GitHub Pages"
git push
```

Depois, siga os passos acima novamente.

---

**O web app deve estar disponível em:**
```
https://kpedro.github.io/NinjaBrain/
```

🥷 **Vamos fazer funcionar!**

