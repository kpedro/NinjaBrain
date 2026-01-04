# 🌐 Como Verificar o Web App NinjaBrain Online

## 🎯 URL do Seu Web App

```
https://kpedro.github.io/NinjaBrain/
```

---

## ✅ Passos Rápidos para Verificar

### 1. Ativar GitHub Pages (se ainda não estiver)

1. Acesse: https://github.com/kpedro/NinjaBrain/settings/pages
2. Em **Source**, escolha:
   - **Opção A:** GitHub Actions (recomendado - já tem workflow configurado)
   - **Opção B:** Deploy from a branch → Branch: `main` → Folder: `/app`
3. Clique em **Save**
4. Aguarde 2-5 minutos

### 2. Verificar se o Deploy Funcionou

1. Acesse: https://github.com/kpedro/NinjaBrain/actions
2. Procure por "Deploy to GitHub Pages"
3. Deve ter um ✅ verde se funcionou

### 3. Acessar o Web App

Abra no navegador:
```
https://kpedro.github.io/NinjaBrain/
```

**O que você deve ver:**
- ✅ Header com "🥷 NinjaBrain"
- ✅ Tabs funcionando (Plano, Disciplinas, Cronograma)
- ✅ Conteúdo do plano.md carregado
- ✅ Design escuro moderno e responsivo

---

## 🧪 Testar Localmente Primeiro (Opcional)

Para garantir que funciona antes de verificar online:

```powershell
cd C:\Users\Kadson\NinjaBrain\app
python -m http.server 8000
```

Depois acesse: http://localhost:8000

---

## 📱 Testar em Diferentes Dispositivos

Depois que estiver online, teste em:
- 💻 Desktop
- 📱 Mobile (celular)
- 🖥️ Tablet

---

## 🐛 Se Não Funcionar

### Problema: Página 404
- Aguarde mais 5 minutos (primeira vez demora)
- Verifique se GitHub Pages está ativado
- Verifique se a pasta `/app` está selecionada

### Problema: Markdown não carrega
- Abra o console (F12) para ver erros
- O arquivo `plano.md` precisa estar na pasta `app/`
- Pode ser problema de CORS (normal no GitHub Pages)

### Problema: Estilos não aparecem
- Verifique se `styles.css` está na pasta `app/`
- Limpe o cache (Ctrl+F5)

---

## 🔄 Atualizar o Web App

Sempre que fizer mudanças:

```bash
cd C:\Users\Kadson\NinjaBrain
git add app/
git commit -m "Atualização do web app"
git push
```

O GitHub Pages atualiza automaticamente em 1-2 minutos.

---

**Pronto! Seu NinjaBrain está no ar! 🥷🌐**

