# 💻 Exemplo Prático: Implementando Chat com IA

## 🎯 Objetivo

Criar um chat assistente no web app que responde perguntas sobre estudos usando Gemini API.

---

## 📦 Passo 1: Configurar Vercel Functions

### **1.1. Instalar Vercel CLI**

```bash
npm install -g vercel
```

### **1.2. Criar Estrutura**

```
NinjaBrain/
  api/
    chat.js          ← Nova pasta e arquivo
  app/
    (arquivos atuais)
  vercel.json        ← Novo arquivo
```

### **1.3. Criar `vercel.json`**

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/**/*.js",
      "use": "@vercel/node"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/$1"
    }
  ]
}
```

---

## 🤖 Passo 2: Criar API de Chat

### **2.1. Criar `api/chat.js`**

```javascript
const { GoogleGenerativeAI } = require('@google/generative-ai');

module.exports = async (req, res) => {
  // Configurar CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { message, perfil } = req.body;

  if (!message) {
    return res.status(400).json({ error: 'Mensagem é obrigatória' });
  }

  const apiKey = process.env.GEMINI_API_KEY;

  if (!apiKey) {
    return res.status(500).json({ error: 'API key não configurada' });
  }

  try {
    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash' });

    // Contexto baseado no perfil
    const contextos = {
      fundamental: 'Você está ajudando um estudante do Ensino Fundamental. Seja claro, use exemplos simples e seja encorajador.',
      medio: 'Você está ajudando um estudante do Ensino Médio preparando para ENEM/Vestibular. Foque em técnicas eficientes e priorização.',
      superior: 'Você está ajudando um estudante universitário. Foque em organização acadêmica e preparação profissional.',
      concurso: 'Você está ajudando um candidato a concurso público. Seja direto, técnico e focado em aprovação. Use a regra 80/20.',
      profissional: 'Você está ajudando um profissional em transição de carreira. Foque em aprendizado acelerado e habilidades práticas.'
    };

    const contexto = contextos[perfil] || contextos.concurso;

    const prompt = `
${contexto}

Você é o NinjaBrain, assistente educacional inteligente.
Sua missão é ajudar o estudante a aprender de forma eficiente.

Pergunta do estudante: ${message}

Responda de forma:
- Direta e objetiva
- Com exemplos práticos quando possível
- Encorajadora e motivadora
- Focada em resultados
`;

    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();

    return res.status(200).json({ 
      resposta: text,
      sucesso: true 
    });

  } catch (error) {
    console.error('Erro na API:', error);
    return res.status(500).json({ 
      error: 'Erro ao processar mensagem',
      detalhes: error.message 
    });
  }
};
```

### **2.2. Instalar Dependência**

Criar `package.json` na raiz:

```json
{
  "name": "ninjabrain",
  "version": "2.0.0",
  "dependencies": {
    "@google/generative-ai": "^0.2.1"
  }
}
```

Instalar:
```bash
npm install
```

---

## 🎨 Passo 3: Adicionar Interface no Frontend

### **3.1. Adicionar HTML ao `app/index.html`**

Antes do `</body>`, adicionar:

```html
<!-- Chat Assistente -->
<div id="chat-container" class="chat-container" style="display: none;">
    <div class="chat-header">
        <h3>🥷 Assistente NinjaBrain</h3>
        <button id="fechar-chat" class="chat-close">×</button>
    </div>
    <div id="chat-messages" class="chat-messages"></div>
    <div class="chat-input-container">
        <input type="text" id="chat-input" placeholder="Pergunte sobre seus estudos..." />
        <button id="enviar-chat" class="chat-send">Enviar</button>
    </div>
</div>
<button id="abrir-chat" class="chat-toggle" title="Abrir assistente">💬</button>
```

### **3.2. Adicionar CSS ao `app/styles.css`**

```css
/* Chat Container */
.chat-container {
    position: fixed;
    bottom: 80px;
    right: 20px;
    width: 350px;
    max-width: calc(100vw - 40px);
    height: 500px;
    background: var(--bg-secondary);
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    display: flex;
    flex-direction: column;
    z-index: 1000;
    border: 1px solid var(--border-color);
}

.chat-header {
    padding: 15px;
    border-bottom: 1px solid var(--border-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--bg-primary);
    border-radius: 12px 12px 0 0;
}

.chat-header h3 {
    margin: 0;
    font-size: 16px;
    color: var(--text-primary);
}

.chat-close {
    background: none;
    border: none;
    color: var(--text-secondary);
    font-size: 24px;
    cursor: pointer;
    padding: 0;
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    transition: background 0.2s;
}

.chat-close:hover {
    background: var(--bg-hover);
}

.chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 15px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.chat-message {
    padding: 10px 15px;
    border-radius: 12px;
    max-width: 80%;
    word-wrap: break-word;
    animation: fadeIn 0.3s;
}

.chat-message.user {
    background: var(--accent-color);
    color: white;
    align-self: flex-end;
    border-bottom-right-radius: 4px;
}

.chat-message.assistant {
    background: var(--bg-primary);
    color: var(--text-primary);
    align-self: flex-start;
    border-bottom-left-radius: 4px;
    border: 1px solid var(--border-color);
}

.chat-input-container {
    padding: 15px;
    border-top: 1px solid var(--border-color);
    display: flex;
    gap: 10px;
    background: var(--bg-primary);
    border-radius: 0 0 12px 12px;
}

#chat-input {
    flex: 1;
    padding: 10px;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    background: var(--bg-secondary);
    color: var(--text-primary);
    font-size: 14px;
}

#chat-input:focus {
    outline: none;
    border-color: var(--accent-color);
}

.chat-send {
    padding: 10px 20px;
    background: var(--accent-color);
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
    transition: opacity 0.2s;
}

.chat-send:hover {
    opacity: 0.9;
}

.chat-send:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.chat-toggle {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: var(--accent-color);
    color: white;
    border: none;
    font-size: 24px;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    z-index: 999;
    transition: transform 0.2s;
}

.chat-toggle:hover {
    transform: scale(1.1);
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Mobile */
@media (max-width: 768px) {
    .chat-container {
        width: calc(100vw - 20px);
        height: calc(100vh - 100px);
        bottom: 70px;
        right: 10px;
    }
}
```

### **3.3. Adicionar JavaScript ao `app/app.js`**

No final do arquivo, adicionar:

```javascript
// ============================================
// CHAT COM IA
// ============================================

let chatInicializado = false;

function inicializarChat() {
    if (chatInicializado) return;
    chatInicializado = true;

    // Event listeners
    document.getElementById('abrir-chat')?.addEventListener('click', () => {
        document.getElementById('chat-container').style.display = 'flex';
    });

    document.getElementById('fechar-chat')?.addEventListener('click', () => {
        document.getElementById('chat-container').style.display = 'none';
    });

    document.getElementById('enviar-chat')?.addEventListener('click', enviarMensagem);
    
    document.getElementById('chat-input')?.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            enviarMensagem();
        }
    });
}

async function enviarMensagem() {
    const input = document.getElementById('chat-input');
    const mensagem = input.value.trim();
    
    if (!mensagem) return;

    // Adiciona mensagem do usuário
    adicionarMensagem('user', mensagem);
    input.value = '';
    
    // Desabilita input
    input.disabled = true;
    document.getElementById('enviar-chat').disabled = true;

    // Mostra loading
    const loadingId = adicionarMensagem('assistant', 'Pensando... 🧠');

    try {
        const perfil = localStorage.getItem('ninjaBrainPerfil') || 'concurso';
        
        // Chama API (ajustar URL para produção)
        const apiUrl = 'https://seu-projeto.vercel.app/api/chat';
        // Para desenvolvimento local: 'http://localhost:3000/api/chat'
        
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: mensagem,
                perfil: perfil
            })
        });

        if (!response.ok) {
            throw new Error('Erro ao chamar API');
        }

        const data = await response.json();
        
        // Remove loading e adiciona resposta
        document.getElementById(loadingId).textContent = data.resposta;
        document.getElementById(loadingId).classList.remove('assistant');
        document.getElementById(loadingId).classList.add('assistant');

    } catch (error) {
        console.error('Erro:', error);
        document.getElementById(loadingId).textContent = 
            'Desculpe, ocorreu um erro. Tente novamente.';
    } finally {
        // Reabilita input
        input.disabled = false;
        document.getElementById('enviar-chat').disabled = false;
        input.focus();
    }
}

function adicionarMensagem(tipo, texto) {
    const messagesDiv = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${tipo}`;
    messageDiv.textContent = texto;
    messageDiv.id = `msg-${Date.now()}`;
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
    return messageDiv.id;
}

// Inicializar quando DOM estiver pronto
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inicializarChat);
} else {
    inicializarChat();
}
```

---

## 🚀 Passo 4: Deploy

### **4.1. Configurar Variável de Ambiente no Vercel**

1. Acesse [vercel.com](https://vercel.com)
2. Crie conta ou faça login
3. Importe o repositório GitHub
4. Em Settings → Environment Variables:
   - Adicione: `GEMINI_API_KEY` = sua chave

### **4.2. Deploy**

```bash
vercel
```

Ou conecte o repositório GitHub no Vercel (deploy automático).

### **4.3. Atualizar URL no Frontend**

No `app/app.js`, atualize a URL da API:

```javascript
const apiUrl = 'https://seu-projeto.vercel.app/api/chat';
```

---

## ✅ Teste

1. Abra o web app
2. Clique no botão 💬 (canto inferior direito)
3. Digite uma pergunta sobre estudos
4. Veja a resposta da IA!

---

## 🐛 Troubleshooting

### **Erro: CORS**
- Verifique se o CORS está configurado na função
- Verifique se a URL da API está correta

### **Erro: API Key não encontrada**
- Verifique se a variável de ambiente está configurada no Vercel
- Verifique se o nome da variável está correto

### **Erro: Função não encontrada**
- Verifique se o arquivo está em `api/chat.js`
- Verifique se o `vercel.json` está correto

---

**Pronto! Agora você tem um chat com IA funcionando! 🎉**

