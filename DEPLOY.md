# 🚀 Guia de Deploy - GitHub Pages

## Passo a Passo Rápido

### 1. Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Nome: `NinjaBrain` (ou o que preferir)
3. Marque como **Público** (para GitHub Pages gratuito)
4. **NÃO** inicialize com README (já temos um)
5. Clique em **Create repository**

---

### 2. Fazer Upload dos Arquivos

#### Opção A: Via Git (Recomendado)

```bash
# Na pasta do projeto
git init
git add .
git commit -m "Initial commit: NinjaBrain web app"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/NinjaBrain.git
git push -u origin main
```

#### Opção B: Via GitHub Web

1. No repositório criado, clique em **uploading an existing file**
2. Arraste toda a pasta do projeto (exceto `.env`)
3. Commit

---

### 3. Ativar GitHub Pages

#### Método 1: Automático (GitHub Actions) ✅

1. Vá em **Settings > Pages**
2. Em **Source**, selecione **GitHub Actions**
3. O workflow `.github/workflows/deploy.yml` fará o deploy automaticamente
4. Aguarde alguns minutos
5. Acesse: `https://SEU-USUARIO.github.io/NinjaBrain/`

#### Método 2: Manual

1. Vá em **Settings > Pages**
2. Em **Source**, selecione **Deploy from a branch**
3. Branch: `main`
4. Folder: `/app`
5. Clique em **Save**
6. Aguarde alguns minutos
7. Acesse: `https://SEU-USUARIO.github.io/NinjaBrain/`

---

### 4. Verificar Deploy

Após alguns minutos, acesse:
```
https://SEU-USUARIO.github.io/NinjaBrain/
```

Se aparecer a página do NinjaBrain, está funcionando! 🎉

---

## ⚠️ Importante

### Arquivos que NÃO devem ir para o Git:

- ✅ `.env` (já está no .gitignore)
- ✅ `__pycache__/`
- ✅ Arquivos temporários

### Arquivos que DEVEM ir:

- ✅ `app/` (toda a pasta)
- ✅ `backend/` (scripts Python)
- ✅ `knowledge/` (conteúdo)
- ✅ `README.md`
- ✅ `.gitignore`
- ✅ `.github/workflows/deploy.yml`

---

## 🔄 Atualizar o Site

Sempre que fizer mudanças:

```bash
git add .
git commit -m "Atualização: descrição das mudanças"
git push
```

O GitHub Pages atualiza automaticamente em 1-2 minutos.

---

## 🐛 Troubleshooting

### Página não aparece?
- Aguarde 5-10 minutos (primeira vez demora mais)
- Verifique se o branch está correto
- Verifique se a pasta `/app` está selecionada

### Erro 404?
- Verifique se o arquivo `app/index.html` existe
- Verifique se o caminho está correto: `/app`

### Markdown não carrega?
- Verifique se `app/plano.md` existe
- Abra o console do navegador (F12) para ver erros

---

## 📱 Acessar de Qualquer Lugar

Depois do deploy, você pode acessar de:
- 💻 Computador
- 📱 Celular
- 🖥️ Tablet

**URL:** `https://SEU-USUARIO.github.io/NinjaBrain/`

---

**Pronto! Seu NinjaBrain está no ar! 🥷**

