# 🤖 Implementação de IA no NinjaBrain

## 📊 Situação Atual

### **O Que Já Existe:**
- ✅ **Gemini API** (`backend/brain.py`) - Assistente CLI para estudos
- ✅ **Perplexity API** (`backend/integrations/search.py`) - Busca na web
- ✅ **Web App Estático** (`app/`) - Frontend no GitHub Pages
- ✅ **Streamlit App** (`app.py`) - App interativo (mencionado)

### **Desafio:**
- Web app é **estático** (GitHub Pages)
- Backend Python não está conectado ao frontend
- IA está apenas em scripts Python locais

---

## 🎯 Funcionalidades de IA Propostas

### **1. Assistente Virtual de Estudos** ⭐ (Prioridade Alta)
**O que faz:**
- Responde perguntas sobre matérias
- Explica conceitos difíceis
- Sugere técnicas de estudo personalizadas
- Ajuda a criar planos de estudo

**Como funciona:**
- Chat integrado no web app
- Usa Gemini/OpenAI/Claude
- Contexto do perfil do usuário

---

### **2. Geração Inteligente de Planos de Estudo** ⭐ (Prioridade Alta)
**O que faz:**
- Cria planos personalizados baseados em:
  - Perfil do usuário
  - Tempo disponível
  - Objetivo (ENEM, Concurso, etc.)
  - Nível atual

**Como funciona:**
- IA analisa inputs do usuário
- Gera cronograma otimizado
- Ajusta baseado em progresso

---

### **3. Recomendações Personalizadas** ⭐ (Prioridade Média)
**O que faz:**
- Sugere técnicas de estudo baseadas em:
  - Matéria que está estudando
  - Estilo de aprendizado
  - Histórico de uso
- Recomenda conteúdos relevantes

**Como funciona:**
- Análise de padrões de uso
- Machine Learning simples
- Feedback do usuário

---

### **4. Análise de Progresso Inteligente** (Prioridade Média)
**O que faz:**
- Analisa tempo de estudo
- Identifica pontos fracos
- Sugere melhorias
- Previsão de tempo para objetivo

**Como funciona:**
- Processa dados de estudo
- Gera insights automáticos
- Relatórios personalizados

---

### **5. Busca Inteligente de Conteúdo** (Prioridade Baixa)
**O que faz:**
- Busca informações atualizadas na web
- Responde perguntas sobre editais
- Atualiza informações de concursos

**Como funciona:**
- Integração Perplexity (já existe)
- Interface no web app

---

## 🏗️ Arquitetura Proposta

### **Opção 1: Serverless Functions (Recomendado para Começar)**

```
Frontend (GitHub Pages)
    ↓
Vercel/Netlify Functions (API Gateway)
    ↓
APIs de IA (Gemini/OpenAI/Claude)
```

**Vantagens:**
- ✅ Não precisa de servidor dedicado
- ✅ Escala automaticamente
- ✅ Gratuito para começar
- ✅ Fácil de implementar

**Desvantagens:**
- ⚠️ Limites de execução (10s-60s)
- ⚠️ Cold start pode ser lento

---

### **Opção 2: Backend Dedicado (Para Escalar)**

```
Frontend (GitHub Pages)
    ↓
Backend API (Python FastAPI / Node.js Express)
    ↓
APIs de IA + Banco de Dados
```

**Vantagens:**
- ✅ Mais controle
- ✅ Sem limites de tempo
- ✅ Pode processar em background
- ✅ Melhor para ML/analytics

**Desvantagens:**
- ⚠️ Precisa de servidor/hosting
- ⚠️ Mais complexo de manter

---

### **Opção 3: Híbrida (Melhor dos Dois Mundos)**

```
Frontend (GitHub Pages)
    ↓
┌─────────────────┬─────────────────┐
│ Serverless      │ Backend Dedicado │
│ (Chat rápido)   │ (Processamento) │
└─────────────────┴─────────────────┘
```

**Uso:**
- Serverless: Chat, respostas rápidas
- Backend: Análise, ML, processamento pesado

---

## 💻 Implementação Prática

### **Fase 1: Chat Assistente (MVP)**

#### **1.1. Criar API Serverless (Vercel Functions)**

**Estrutura:**
```
api/
  chat.js (ou chat.py)
```

**Exemplo (Node.js):**
```javascript
// api/chat.js
import { GoogleGenerativeAI } from '@google/generative-ai';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { message, perfil } = req.body;
  const apiKey = process.env.GEMINI_API_KEY;

  try {
    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash' });

    const contexto = `
      Você é o NinjaBrain, assistente educacional inteligente.
      Perfil do usuário: ${perfil}
      Seja direto, técnico e focado em resultados.
    `;

    const result = await model.generateContent(`${contexto}\n\nPergunta: ${message}`);
    const response = await result.response;
    const text = response.text();

    return res.status(200).json({ resposta: text });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
}
```

#### **1.2. Integrar no Frontend**

**Adicionar ao `app/app.js`:**
```javascript
// Função para chat com IA
async function enviarMensagemChat(mensagem) {
    const perfil = localStorage.getItem('ninjaBrainPerfil') || 'concurso';
    
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                message: mensagem,
                perfil: perfil 
            })
        });
        
        const data = await response.json();
        return data.resposta;
    } catch (error) {
        console.error('Erro ao chamar IA:', error);
        return 'Desculpe, ocorreu um erro. Tente novamente.';
    }
}

// Adicionar interface de chat no HTML
function criarInterfaceChat() {
    const chatHTML = `
        <div id="chat-container" class="chat-container">
            <div class="chat-header">
                <h3>🥷 Assistente NinjaBrain</h3>
                <button id="fechar-chat">×</button>
            </div>
            <div id="chat-messages" class="chat-messages"></div>
            <div class="chat-input-container">
                <input type="text" id="chat-input" placeholder="Pergunte algo sobre seus estudos...">
                <button id="enviar-chat">Enviar</button>
            </div>
        </div>
        <button id="abrir-chat" class="chat-toggle">💬</button>
    `;
    
    document.body.insertAdjacentHTML('beforeend', chatHTML);
    
    // Event listeners
    document.getElementById('abrir-chat').addEventListener('click', () => {
        document.getElementById('chat-container').style.display = 'flex';
    });
    
    document.getElementById('enviar-chat').addEventListener('click', async () => {
        const input = document.getElementById('chat-input');
        const mensagem = input.value;
        if (!mensagem) return;
        
        // Adiciona mensagem do usuário
        adicionarMensagemChat('user', mensagem);
        input.value = '';
        
        // Mostra loading
        const loadingId = adicionarMensagemChat('assistant', 'Pensando...');
        
        // Chama IA
        const resposta = await enviarMensagemChat(mensagem);
        
        // Atualiza com resposta
        document.getElementById(loadingId).textContent = resposta;
    });
}

function adicionarMensagemChat(tipo, texto) {
    const messagesDiv = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${tipo}`;
    messageDiv.textContent = texto;
    messageDiv.id = `msg-${Date.now()}`;
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
    return messageDiv.id;
}
```

---

### **Fase 2: Geração de Planos Inteligentes**

#### **2.1. API de Geração de Planos**

```javascript
// api/gerar-plano.js
import { GoogleGenerativeAI } from '@google/generative-ai';

export default async function handler(req, res) {
  const { perfil, objetivo, tempoDisponivel, prazo } = req.body;

  const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
  const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash' });

  const prompt = `
    Crie um plano de estudos personalizado em formato JSON:
    - Perfil: ${perfil}
    - Objetivo: ${objetivo}
    - Tempo disponível: ${tempoDisponivel} horas/semana
    - Prazo: ${prazo} dias
    
    Retorne um JSON com:
    {
      "semanas": [
        {
          "numero": 1,
          "foco": "Fundação",
          "disciplinas": [
            {"nome": "Matemática", "horas": 5, "topics": ["Funções", "Álgebra"]}
          ]
        }
      ]
    }
  `;

  const result = await model.generateContent(prompt);
  const response = await result.response;
  
  // Parse JSON da resposta
  const plano = JSON.parse(response.text());
  
  return res.status(200).json({ plano });
}
```

#### **2.2. Interface no Frontend**

```javascript
// Adicionar formulário de geração de plano
function criarFormularioPlano() {
    const formHTML = `
        <div id="gerar-plano-modal" class="modal">
            <div class="modal-content">
                <h2>Gerar Plano Personalizado</h2>
                <form id="form-plano">
                    <label>Objetivo:</label>
                    <input type="text" id="objetivo" placeholder="Ex: Passar no ENEM 2025">
                    
                    <label>Tempo disponível (horas/semana):</label>
                    <input type="number" id="tempo" min="1" max="40" value="10">
                    
                    <label>Prazo (dias):</label>
                    <input type="number" id="prazo" min="7" max="365" value="180">
                    
                    <button type="submit">Gerar Plano</button>
                </form>
            </div>
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', formHTML);
    
    document.getElementById('form-plano').addEventListener('submit', async (e) => {
        e.preventDefault();
        const perfil = localStorage.getItem('ninjaBrainPerfil');
        const objetivo = document.getElementById('objetivo').value;
        const tempo = document.getElementById('tempo').value;
        const prazo = document.getElementById('prazo').value;
        
        // Chama API
        const response = await fetch('/api/gerar-plano', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ perfil, objetivo, tempoDisponivel: tempo, prazo })
        });
        
        const { plano } = await response.json();
        
        // Renderiza plano gerado
        renderizarPlanoGerado(plano);
    });
}
```

---

### **Fase 3: Recomendações Personalizadas**

#### **3.1. Sistema de Análise de Padrões**

```javascript
// Armazena histórico de uso no LocalStorage
function salvarSessaoEstudo(disciplina, tecnica, duracao) {
    const historico = JSON.parse(localStorage.getItem('historicoEstudos') || '[]');
    historico.push({
        data: new Date().toISOString(),
        disciplina,
        tecnica,
        duracao
    });
    localStorage.setItem('historicoEstudos', JSON.stringify(historico));
}

// Analisa padrões e gera recomendações
async function gerarRecomendacoes() {
    const historico = JSON.parse(localStorage.getItem('historicoEstudos') || '[]');
    const perfil = localStorage.getItem('ninjaBrainPerfil');
    
    // Envia para IA analisar
    const response = await fetch('/api/recomendacoes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ historico, perfil })
    });
    
    const { recomendacoes } = await response.json();
    return recomendacoes;
}
```

---

## 🔧 Configuração Técnica

### **1. Vercel Functions (Recomendado)**

**Estrutura:**
```
projeto/
  api/
    chat.js
    gerar-plano.js
    recomendacoes.js
  app/
    (frontend atual)
  vercel.json
```

**vercel.json:**
```json
{
  "functions": {
    "api/**/*.js": {
      "runtime": "nodejs18.x"
    }
  },
  "env": {
    "GEMINI_API_KEY": "@gemini_api_key"
  }
}
```

**Deploy:**
```bash
npm install -g vercel
vercel
```

---

### **2. Netlify Functions (Alternativa)**

**Estrutura:**
```
netlify/
  functions/
    chat.js
    gerar-plano.js
```

**netlify.toml:**
```toml
[build]
  functions = "netlify/functions"

[build.environment]
  GEMINI_API_KEY = "sua_chave"
```

---

### **3. Backend Python (Para Processamento Pesado)**

**Estrutura:**
```
backend/
  api/
    main.py (FastAPI)
    routes/
      chat.py
      planos.py
```

**main.py:**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

@app.post("/api/chat")
async def chat(request: dict):
    mensagem = request.get("message")
    perfil = request.get("perfil", "concurso")
    
    contexto = f"Você é o NinjaBrain. Perfil: {perfil}"
    response = model.generate_content(f"{contexto}\n\n{mensagem}")
    
    return {"resposta": response.text}
```

**Deploy:**
- Railway.app (gratuito)
- Render.com (gratuito)
- Fly.io (gratuito)

---

## 📋 Roadmap de Implementação

### **Sprint 1 (1-2 semanas): Chat Básico**
- [ ] Criar API serverless (Vercel/Netlify)
- [ ] Integrar Gemini API
- [ ] Criar interface de chat no frontend
- [ ] Testar e ajustar

### **Sprint 2 (1-2 semanas): Geração de Planos**
- [ ] API de geração de planos
- [ ] Formulário no frontend
- [ ] Renderização de planos gerados
- [ ] Salvar planos no LocalStorage

### **Sprint 3 (2-3 semanas): Recomendações**
- [ ] Sistema de tracking de uso
- [ ] API de análise de padrões
- [ ] Interface de recomendações
- [ ] Feedback do usuário

### **Sprint 4 (2-3 semanas): Análise de Progresso**
- [ ] Coleta de dados de estudo
- [ ] Análise com IA
- [ ] Dashboard de insights
- [ ] Relatórios personalizados

---

## 💰 Custos Estimados

### **Gratuito (Para Começar):**
- ✅ Vercel Functions: 100GB-hora/mês grátis
- ✅ Gemini API: 15 requisições/minuto grátis
- ✅ Netlify Functions: 125k invocações/mês grátis

### **Custos com Escala:**
- Gemini API: ~$0.00025 por requisição
- Vercel: $20/mês (Pro)
- Backend: $5-20/mês (Railway/Render)

**Estimativa para 1000 usuários/mês:**
- ~$10-30/mês total

---

## 🔐 Segurança

### **Boas Práticas:**
1. **Nunca exponha chaves no frontend**
   - Use variáveis de ambiente
   - Serverless functions protegem chaves

2. **Rate Limiting**
   - Limite de requisições por usuário
   - Previne abuso

3. **Validação de Input**
   - Sanitize mensagens do usuário
   - Valide dados antes de enviar para IA

4. **CORS Configurado**
   - Apenas domínios permitidos
   - Não use `allow_origins: ["*"]` em produção

---

## 🚀 Próximos Passos Imediatos

1. **Escolher plataforma:** Vercel ou Netlify
2. **Criar primeira função:** Chat básico
3. **Testar localmente:** Verificar funcionamento
4. **Integrar frontend:** Adicionar interface de chat
5. **Deploy:** Colocar no ar
6. **Testar com usuários:** Coletar feedback

---

## 📚 Recursos Úteis

- [Vercel Functions Docs](https://vercel.com/docs/functions)
- [Netlify Functions Docs](https://docs.netlify.com/functions/overview/)
- [Gemini API Docs](https://ai.google.dev/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com/)

---

**Pronto para começar a implementar IA no NinjaBrain! 🚀**

