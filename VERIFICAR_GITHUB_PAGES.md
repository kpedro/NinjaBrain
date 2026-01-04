# 🌐 Verificar e Ativar GitHub Pages - NinjaBrain

## 📍 URL Esperada

Seu web app deve estar disponível em:
```
https://kpedro.github.io/NinjaBrain/
```

---

## ✅ Passo 1: Verificar se GitHub Pages está Ativado

1. **Acesse o repositório no GitHub:**
   - https://github.com/kpedro/NinjaBrain

2. **Vá em Settings:**
   - Clique em **Settings** (no topo do repositório)

3. **Vá em Pages:**
   - No menu lateral esquerdo, clique em **Pages**

4. **Verifique a configuração:**
   - **Source:** Deve estar como "GitHub Actions" ou "Deploy from a branch"
   - Se estiver desativado, veja o Passo 2

---

## 🔧 Passo 2: Ativar GitHub Pages (se não estiver ativo)

### Opção A: GitHub Actions (Recomendado) ✅

1. Em **Settings > Pages**
2. Em **Source**, selecione: **GitHub Actions**
3. Clique em **Save**
4. O workflow `.github/workflows/deploy.yml` fará o deploy automaticamente
5. Aguarde 2-5 minutos

### Opção B: Deploy Manual

1. Em **Settings > Pages**
2. Em **Source**, selecione: **Deploy from a branch**
3. **Branch:** `main`
4. **Folder:** `/app`
5. Clique em **Save**
6. Aguarde 2-5 minutos

---

## 🧪 Passo 3: Testar Localmente (Antes de Verificar Online)

Para garantir que o web app funciona, teste localmente:

```powershell
cd C:\Users\Kadson\NinjaBrain\app
python -m http.server 8000
```

Depois acesse no navegador:
```
http://localhost:8000
```

**O que você deve ver:**
- ✅ Header com "🥷 NinjaBrain"
- ✅ Tabs: Plano de Ataque, Disciplinas, Cronograma
- ✅ Conteúdo do plano.md carregado
- ✅ Design escuro moderno

---

## 🔍 Passo 4: Verificar Deploy no GitHub

1. **Vá em Actions:**
   - No repositório, clique em **Actions** (no topo)
   - Procure por "Deploy to GitHub Pages"
   - Deve ter um ✅ verde se funcionou

2. **Verifique os logs:**
   - Clique no workflow mais recente
   - Veja se todos os steps passaram

---

## 🌐 Passo 5: Acessar o Web App Online

Após ativar o GitHub Pages, acesse:

```
https://kpedro.github.io/NinjaBrain/
```

**Tempo de espera:**
- Primeira vez: 5-10 minutos
- Atualizações: 1-2 minutos

---

## 🐛 Problemas Comuns

### ❌ Página não carrega (404)

**Soluções:**
1. Aguarde mais 5 minutos (primeira vez demora)
2. Verifique se a pasta `/app` está selecionada
3. Verifique se o branch é `main`
4. Verifique se o workflow rodou com sucesso

### ❌ Markdown não aparece

**Soluções:**
1. Abra o console do navegador (F12)
2. Veja se há erros de CORS
3. Verifique se `app/plano.md` está no repositório
4. O GitHub Pages pode bloquear fetch de arquivos locais

**Solução para CORS:**
- O arquivo `plano.md` precisa estar no mesmo domínio
- Se não funcionar, podemos converter para HTML estático

### ❌ Estilos não carregam

**Soluções:**
1. Verifique se `app/styles.css` está no repositório
2. Verifique o caminho no HTML: `href="styles.css"`
3. Limpe o cache do navegador (Ctrl+F5)

---

## 📱 Testar em Diferentes Dispositivos

Depois que estiver online, teste em:
- 💻 Desktop
- 📱 Mobile (celular)
- 🖥️ Tablet

O design é responsivo e deve funcionar em todos!

---

## 🔄 Atualizar o Site

Sempre que fizer mudanças no web app:

```bash
cd C:\Users\Kadson\NinjaBrain
git add app/
git commit -m "Atualização do web app"
git push
```

O GitHub Pages atualiza automaticamente em 1-2 minutos.

---

## ✅ Checklist Final

- [ ] GitHub Pages ativado em Settings
- [ ] Source configurado (GitHub Actions ou Branch)
- [ ] Workflow rodou com sucesso (Actions)
- [ ] URL acessível: https://kpedro.github.io/NinjaBrain/
- [ ] Web app carrega corretamente
- [ ] Tabs funcionam
- [ ] Markdown aparece
- [ ] Design responsivo funciona

---

**Pronto! Seu NinjaBrain está no ar! 🥷🌐**

