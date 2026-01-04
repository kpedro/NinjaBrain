# 🧪 Guia de Teste - Novas Funcionalidades

## 🚀 Como Testar

### **1. Iniciar Servidor Local**

```powershell
cd C:\Users\Kadson\NinjaBrain\app
python -m http.server 8000
```

Depois acesse: **http://localhost:8000**

---

## ✅ Checklist de Testes

### **Teste 1: Onboarding (Seleção de Perfil)**

- [ ] Ao abrir pela primeira vez, aparece tela de seleção de perfil
- [ ] Todos os 5 perfis aparecem como cards
- [ ] Cada card mostra: ícone, nome, descrição e botão
- [ ] Ao clicar em "Escolher este perfil", a tela principal aparece
- [ ] Ao clicar em "Pular e usar modo padrão", usa perfil de concurso

**Perfis para testar:**
- 📚 Ensino Fundamental
- 🎓 Ensino Médio
- 🎓 Ensino Superior
- 🏆 Concurso Público
- 💼 Profissional/Transição

---

### **Teste 2: Interface Adaptada ao Perfil**

- [ ] Header mostra ícone e nome do perfil selecionado
- [ ] Subtítulo muda conforme o perfil
- [ ] Botão "Trocar perfil" aparece no header
- [ ] Ao clicar em "Trocar perfil", volta para onboarding

---

### **Teste 3: Nova Aba "Técnicas de Estudo"**

- [ ] Aba "📖 Técnicas de Estudo" aparece na navegação
- [ ] Ao clicar, mostra grid com todas as técnicas
- [ ] Cada card mostra: ícone, nome, nível, categoria, descrição
- [ ] Botão "Ver detalhes" em cada card

---

### **Teste 4: Filtros de Técnicas**

- [ ] Filtro "Todas" mostra todas as 11 técnicas
- [ ] Filtro "Fundamental" mostra apenas técnicas fundamentais
- [ ] Filtro "Intermediário" mostra apenas técnicas intermediárias
- [ ] Filtro "Avançado" mostra apenas técnicas avançadas
- [ ] Filtro ativo fica destacado

---

### **Teste 5: Modal de Detalhes**

- [ ] Ao clicar em "Ver detalhes", abre modal
- [ ] Modal mostra:
  - ✅ Ícone grande
  - ✅ Nome e badges (nível, categoria)
  - ✅ Descrição completa
  - ✅ Como funciona (passo a passo)
  - ✅ Benefícios (lista)
  - ✅ Quando usar
  - ✅ Base científica
- [ ] Botão X fecha o modal
- [ ] Clicar fora do modal fecha o modal

---

### **Teste 6: Funcionalidades Existentes (Não Quebrar)**

- [ ] Aba "Plano de Ataque" ainda funciona
- [ ] Markdown do plano.md carrega corretamente
- [ ] Aba "Disciplinas" mostra os cards
- [ ] Aba "Cronograma" mostra a timeline
- [ ] Navegação entre abas funciona normalmente

---

### **Teste 7: Responsividade**

- [ ] Testar em tela grande (desktop)
- [ ] Testar em tela média (tablet)
- [ ] Testar em tela pequena (mobile)
- [ ] Grids se adaptam ao tamanho da tela
- [ ] Modal funciona bem em mobile

---

### **Teste 8: Persistência de Dados**

- [ ] Selecionar um perfil
- [ ] Fechar e reabrir o navegador
- [ ] Perfil selecionado deve ser mantido
- [ ] Não deve mostrar onboarding novamente

---

## 🐛 Problemas Conhecidos a Verificar

### **Se onboarding não aparecer:**
- Limpar localStorage: `localStorage.clear()` no console
- Recarregar a página

### **Se técnicas não aparecerem:**
- Verificar console do navegador (F12) para erros
- Verificar se `tecnicas.js` está carregando

### **Se modal não abrir:**
- Verificar se JavaScript está habilitado
- Verificar console para erros

---

## 📊 Resultados Esperados

### **Técnicas por Nível:**

**Fundamental (4):**
- Pomodoro
- Active Recall
- Mind Mapping
- Chunking

**Intermediário (5):**
- Feynman
- Spaced Repetition
- Elaboration
- Dual Coding
- Self-Explanation

**Avançado (1):**
- Interleaving

**Outra (1):**
- Retrieval Practice (pode aparecer em múltiplos)

---

## ✅ Critérios de Sucesso

- ✅ Onboarding funciona na primeira visita
- ✅ Perfis podem ser selecionados e trocados
- ✅ Todas as 11 técnicas aparecem
- ✅ Filtros funcionam corretamente
- ✅ Modal mostra detalhes completos
- ✅ Funcionalidades antigas ainda funcionam
- ✅ Design responsivo funciona
- ✅ Dados persistem entre sessões

---

**Boa sorte nos testes! 🧪**

