// ============================================
// SISTEMA DE PERFIS E ONBOARDING
// ============================================

let perfilAtual = null;

// Verifica se há perfil salvo
function verificarPerfil() {
    const perfilSalvo = obterPerfilSalvo();
    if (perfilSalvo) {
        perfilAtual = getPerfil(perfilSalvo);
        mostrarConteudoPrincipal();
    } else {
        mostrarOnboarding();
    }
}

// Mostra tela de onboarding
function mostrarOnboarding() {
    document.getElementById('onboarding').style.display = 'flex';
    document.getElementById('main-container').style.display = 'none';
    renderizarPerfis();
}

// Mostra conteúdo principal
function mostrarConteudoPrincipal() {
    document.getElementById('onboarding').style.display = 'none';
    document.getElementById('main-container').style.display = 'block';
    
    if (perfilAtual) {
        atualizarInterfacePorPerfil();
        document.getElementById('trocar-perfil').style.display = 'inline-flex';
    }
}

// Renderiza cards de perfis
function renderizarPerfis() {
    const container = document.getElementById('perfis-container');
    container.innerHTML = '';
    
    Object.values(perfisUsuario).forEach(perfil => {
        const card = document.createElement('div');
        card.className = 'perfil-card';
        card.style.borderLeftColor = perfil.cor;
        card.innerHTML = `
            <div class="perfil-icone">${perfil.icone}</div>
            <h3>${perfil.nome}</h3>
            <p>${perfil.descricao}</p>
            <button class="btn-primary" onclick="selecionarPerfil('${perfil.id}')">
                Escolher este perfil
            </button>
        `;
        container.appendChild(card);
    });
}

// Seleciona um perfil
function selecionarPerfil(perfilId) {
    perfilAtual = getPerfil(perfilId);
    salvarPerfil(perfilId);
    mostrarConteudoPrincipal();
}

// Atualiza interface baseada no perfil
function atualizarInterfacePorPerfil() {
    if (!perfilAtual) return;
    
    document.getElementById('perfil-icone').textContent = perfilAtual.icone;
    document.getElementById('perfil-nome').textContent = perfilAtual.nome;
    document.getElementById('subtitle').textContent = perfilAtual.descricao;
}

// Trocar perfil
document.addEventListener('DOMContentLoaded', () => {
    const btnTrocarPerfil = document.getElementById('trocar-perfil');
    if (btnTrocarPerfil) {
        btnTrocarPerfil.addEventListener('click', () => {
            if (confirm('Deseja trocar de perfil? Suas preferências serão atualizadas.')) {
                limparPerfil();
                mostrarOnboarding();
            }
        });
    }

    const btnPular = document.getElementById('pular-onboarding');
    if (btnPular) {
        btnPular.addEventListener('click', () => {
            // Usa perfil de concurso como padrão
            selecionarPerfil('concurso');
        });
    }
});

// ============================================
// CARREGAMENTO DE MARKDOWN
// ============================================

async function loadMarkdown() {
    try {
        const response = await fetch('plano.md');
        const markdown = await response.text();
        const html = marked.parse(markdown);
        document.getElementById('markdown-content').innerHTML = html;
    } catch (error) {
        console.error('Erro ao carregar markdown:', error);
        document.getElementById('markdown-content').innerHTML = 
            '<p>Erro ao carregar o conteúdo. Certifique-se de que o arquivo markdown está no caminho correto.</p>';
    }
}

// ============================================
// SISTEMA DE TABS
// ============================================

function inicializarTabs() {
    const tabs = document.querySelectorAll('.tab');
    const tabContents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetTab = tab.getAttribute('data-tab');

            // Remove active de todos
            tabs.forEach(t => t.classList.remove('active'));
            tabContents.forEach(tc => tc.classList.remove('active'));

            // Adiciona active no selecionado
            tab.classList.add('active');
            const targetContent = document.getElementById(targetTab);
            if (targetContent) {
                targetContent.classList.add('active');
                
                // Carrega conteúdo específico se necessário
                if (targetTab === 'tecnicas' && !targetContent.querySelector('.tecnica-card')) {
                    renderizarTecnicas();
                }
            }
        });
    });
}

// ============================================
// BIBLIOTECA DE TÉCNICAS
// ============================================

let filtroAtual = 'todas';

function renderizarTecnicas(filtro = 'todas') {
    const container = document.getElementById('tecnicas-container');
    if (!container) return;
    
    filtroAtual = filtro;
    const tecnicas = filtrarTecnicas(filtro);
    
    container.innerHTML = '';
    
    if (tecnicas.length === 0) {
        container.innerHTML = '<p class="sem-resultados">Nenhuma técnica encontrada.</p>';
        return;
    }
    
    tecnicas.forEach(tecnica => {
        const card = document.createElement('div');
        card.className = 'tecnica-card';
        card.innerHTML = `
            <div class="tecnica-header-card">
                <span class="tecnica-icone">${tecnica.icone}</span>
                <div>
                    <h3>${tecnica.nome}</h3>
                    <span class="tecnica-badge nivel-${tecnica.nivel.toLowerCase().replace('á', 'a')}">${tecnica.nivel}</span>
                    <span class="tecnica-categoria">${tecnica.categoria}</span>
                </div>
            </div>
            <p class="tecnica-descricao">${tecnica.descricao}</p>
            <button class="btn-ver-detalhes" onclick="mostrarDetalhesTecnica('${tecnica.id}')">
                Ver detalhes →
            </button>
        `;
        container.appendChild(card);
    });
}

function mostrarDetalhesTecnica(tecnicaId) {
    const tecnica = getTecnica(tecnicaId);
    if (!tecnica) return;
    
    const modal = document.getElementById('tecnica-modal');
    const detalhes = document.getElementById('tecnica-detalhes');
    
    detalhes.innerHTML = `
        <div class="tecnica-detalhes-header">
            <span class="tecnica-icone-grande">${tecnica.icone}</span>
            <div>
                <h2>${tecnica.nome}</h2>
                <div class="tecnica-meta">
                    <span class="tecnica-badge nivel-${tecnica.nivel.toLowerCase().replace('á', 'a')}">${tecnica.nivel}</span>
                    <span class="tecnica-categoria">${tecnica.categoria}</span>
                </div>
            </div>
        </div>
        
        <div class="tecnica-secao">
            <h3>📝 Descrição</h3>
            <p>${tecnica.descricao}</p>
        </div>
        
        <div class="tecnica-secao">
            <h3>⚙️ Como Funciona</h3>
            <ol class="tecnica-lista">
                ${tecnica.comoFunciona.map(passo => `<li>${passo}</li>`).join('')}
            </ol>
        </div>
        
        <div class="tecnica-secao">
            <h3>✅ Benefícios</h3>
            <ul class="tecnica-lista">
                ${tecnica.beneficios.map(beneficio => `<li>${beneficio}</li>`).join('')}
            </ul>
        </div>
        
        <div class="tecnica-secao">
            <h3>🎯 Quando Usar</h3>
            <p>${tecnica.quandoUsar}</p>
        </div>
        
        <div class="tecnica-secao">
            <h3>🔬 Base Científica</h3>
            <p class="tecnica-ciencia">${tecnica.ciencia}</p>
        </div>
    `;
    
    modal.style.display = 'flex';
}

function fecharModal() {
    document.getElementById('tecnica-modal').style.display = 'none';
}

// Filtros de técnicas
function inicializarFiltros() {
    const filtros = document.querySelectorAll('.filtro-btn');
    filtros.forEach(btn => {
        btn.addEventListener('click', () => {
            filtros.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filtro = btn.getAttribute('data-filtro');
            renderizarTecnicas(filtro);
        });
    });
}

// ============================================
// INICIALIZAÇÃO
// ============================================

document.addEventListener('DOMContentLoaded', () => {
    // Verifica perfil e mostra onboarding se necessário
    verificarPerfil();
    
    // Inicializa sistema de tabs
    inicializarTabs();
    
    // Carrega markdown (se estiver na aba de plano)
    if (document.getElementById('plano')?.classList.contains('active')) {
        loadMarkdown();
    }
    
    // Inicializa filtros de técnicas
    inicializarFiltros();
    
    // Fecha modal ao clicar no X
    const modalClose = document.querySelector('.modal-close');
    if (modalClose) {
        modalClose.addEventListener('click', fecharModal);
    }
    
    // Fecha modal ao clicar fora
    const modal = document.getElementById('tecnica-modal');
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                fecharModal();
            }
        });
    }
});

// ============================================
// CHAT ASSISTENTE COM IA
// ============================================

let chatInicializado = false;

// URL da API - ajustar conforme ambiente
// Para produção: usar URL do Vercel/Netlify após deploy
// Para desenvolvimento local: usar 'http://localhost:3000/api/chat' (com vercel dev)
// IMPORTANTE: Atualize esta URL após fazer deploy no Vercel!
const API_CHAT_URL = 'https://SEU-PROJETO.vercel.app/api/chat'; // ⚠️ ATUALIZAR APÓS DEPLOY

function inicializarChat() {
    if (chatInicializado) return;
    chatInicializado = true;

    const abrirChatBtn = document.getElementById('abrir-chat');
    const fecharChatBtn = document.getElementById('fechar-chat');
    const enviarChatBtn = document.getElementById('enviar-chat');
    const chatInput = document.getElementById('chat-input');
    const chatContainer = document.getElementById('chat-container');

    if (!abrirChatBtn || !fecharChatBtn || !enviarChatBtn || !chatInput || !chatContainer) {
        console.warn('Elementos do chat não encontrados');
        return;
    }

    // Abrir chat
    abrirChatBtn.addEventListener('click', () => {
        chatContainer.style.display = 'flex';
        chatInput.focus();
    });

    // Fechar chat
    fecharChatBtn.addEventListener('click', () => {
        chatContainer.style.display = 'none';
    });

    // Enviar mensagem (botão)
    enviarChatBtn.addEventListener('click', enviarMensagem);

    // Enviar mensagem (Enter)
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            enviarMensagem();
        }
    });
}

async function enviarMensagem() {
    const input = document.getElementById('chat-input');
    const enviarBtn = document.getElementById('enviar-chat');
    const mensagem = input.value.trim();
    
    if (!mensagem) return;

    // Adiciona mensagem do usuário
    adicionarMensagemChat('user', mensagem);
    input.value = '';
    
    // Desabilita input e botão
    input.disabled = true;
    enviarBtn.disabled = true;

    // Mostra loading
    const loadingId = adicionarMensagemChat('assistant', 'Pensando... 🧠', true);

    try {
        const perfil = localStorage.getItem('ninjaBrainPerfil') || 'concurso';
        
        // Chama API
        const response = await fetch(API_CHAT_URL, {
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
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error || `Erro HTTP: ${response.status}`);
        }

        const data = await response.json();
        
        // Remove loading e adiciona resposta
        const loadingMsg = document.getElementById(loadingId);
        if (loadingMsg) {
            loadingMsg.textContent = data.resposta || 'Desculpe, não consegui gerar uma resposta.';
            loadingMsg.classList.remove('loading');
        } else {
            // Fallback se elemento não existir
            adicionarMensagemChat('assistant', data.resposta || 'Erro ao processar resposta.');
        }

    } catch (error) {
        console.error('Erro ao chamar API:', error);
        
        // Remove loading e mostra erro
        const loadingMsg = document.getElementById(loadingId);
        if (loadingMsg) {
            loadingMsg.textContent = 'Desculpe, ocorreu um erro. Verifique sua conexão e tente novamente.';
            loadingMsg.classList.remove('loading');
        } else {
            adicionarMensagemChat('assistant', 'Erro ao conectar com o assistente. Tente novamente mais tarde.');
        }
    } finally {
        // Reabilita input e botão
        input.disabled = false;
        enviarBtn.disabled = false;
        input.focus();
    }
}

function adicionarMensagemChat(tipo, texto, isLoading = false) {
    const messagesDiv = document.getElementById('chat-messages');
    if (!messagesDiv) return null;

    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${tipo}${isLoading ? ' loading' : ''}`;
    messageDiv.textContent = texto;
    messageDiv.id = `msg-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
    
    messagesDiv.appendChild(messageDiv);
    
    // Scroll para baixo
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
    
    return messageDiv.id;
}

// Inicializar chat quando DOM estiver pronto
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        // Aguardar um pouco para garantir que outros scripts carregaram
        setTimeout(inicializarChat, 100);
    });
} else {
    setTimeout(inicializarChat, 100);
}
