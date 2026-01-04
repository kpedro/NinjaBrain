# 🚀 Ativar GitHub Pages - Passo a Passo

## ⚠️ Problema Atual

Você está vendo um erro 404 porque o GitHub Pages ainda não está ativado.

---

## ✅ Solução: Ativar GitHub Pages

### Passo 1: Acessar Configurações

1. **Abra este link:**
   ```
   https://github.com/kpedro/NinjaBrain/settings/pages
   ```

2. **Ou navegue manualmente:**
   - Acesse: https://github.com/kpedro/NinjaBrain
   - Clique em **Settings** (no topo do repositório)
   - No menu lateral, clique em **Pages**

---

### Passo 2: Configurar a Fonte

Você tem **2 opções**:

#### **Opção A: GitHub Actions (Recomendado) ✅**

1. Em **Source**, selecione: **GitHub Actions**
2. Clique em **Save**
3. O workflow `.github/workflows/deploy.yml` fará o deploy automaticamente
4. Aguarde 2-5 minutos

**Vantagens:**
- ✅ Automático a cada push
- ✅ Já está configurado
- ✅ Mais moderno

#### **Opção B: Deploy Manual**

1. Em **Source**, selecione: **Deploy from a branch**
2. **Branch:** Selecione `main`
3. **Folder:** Selecione `/app`
4. Clique em **Save**
5. Aguarde 2-5 minutos

---

### Passo 3: Verificar o Deploy

1. **Acesse Actions:**
   ```
   https://github.com/kpedro/NinjaBrain/actions
   ```

2. **Procure por:**
   - "Deploy to GitHub Pages" (se usou Opção A)
   - Ou verifique se há um workflow rodando

3. **Aguarde:**
   - Primeira vez: 5-10 minutos
   - Atualizações: 1-2 minutos

---

### Passo 4: Acessar o Web App

Depois de alguns minutos, acesse:

```
https://kpedro.github.io/NinjaBrain/
```

**O que você deve ver:**
- ✅ Header com "🥷 NinjaBrain"
- ✅ Tabs funcionando
- ✅ Conteúdo carregado
- ✅ Design escuro moderno

---

## 🐛 Se Ainda Não Funcionar

### Problema: Ainda mostra 404

**Soluções:**
1. Aguarde mais 5 minutos (primeira vez demora muito)
2. Verifique se o branch é `main`
3. Verifique se a pasta `/app` está selecionada
4. Verifique se os arquivos estão no repositório:
   - `app/index.html`
   - `app/styles.css`
   - `app/app.js`
   - `app/plano.md`

### Problema: Workflow falhou

1. Acesse: https://github.com/kpedro/NinjaBrain/actions
2. Clique no workflow que falhou
3. Veja os logs para identificar o erro
4. Me avise qual erro apareceu

---

## 📸 Screenshot do que você deve ver nas Settings

**Source:** GitHub Actions ou Deploy from a branch
**Branch:** main
**Folder:** /app (se usar Deploy from a branch)

---

## ✅ Checklist

- [ ] Acessei https://github.com/kpedro/NinjaBrain/settings/pages
- [ ] Selecionei a fonte (GitHub Actions ou Deploy from a branch)
- [ ] Configurei branch `main` e pasta `/app` (se necessário)
- [ ] Cliquei em **Save**
- [ ] Aguardei 5-10 minutos
- [ ] Acessei https://kpedro.github.io/NinjaBrain/
- [ ] O web app apareceu! 🎉

---

**Depois de ativar, o web app estará disponível em:**
```
https://kpedro.github.io/NinjaBrain/
```

🥷 **Boa sorte!**

