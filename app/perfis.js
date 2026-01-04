// Sistema de Perfis de Usuário
const perfisUsuario = {
    fundamental: {
        id: 'fundamental',
        nome: 'Ensino Fundamental',
        icone: '📚',
        descricao: 'Organização de estudos, técnicas de memorização e preparação para provas escolares.',
        objetivos: [
            'Organizar estudos diários',
            'Melhorar notas',
            'Desenvolver hábitos de estudo',
            'Preparar para provas escolares'
        ],
        tecnicasRecomendadas: ['pomodoro', 'active-recall', 'mind-mapping', 'chunking'],
        cor: '#10b981' // verde
    },
    medio: {
        id: 'medio',
        nome: 'Ensino Médio',
        icone: '🎓',
        descricao: 'Preparação para ENEM/Vestibular, escolha de carreira e técnicas avançadas de estudo.',
        objetivos: [
            'Preparar para ENEM',
            'Preparar para Vestibular',
            'Escolher carreira',
            'Organizar múltiplas disciplinas'
        ],
        tecnicasRecomendadas: ['pomodoro', 'feynman', 'spaced-repetition', 'active-recall', 'retrieval-practice'],
        cor: '#6366f1' // azul/roxo
    },
    superior: {
        id: 'superior',
        nome: 'Ensino Superior',
        icone: '🎓',
        descricao: 'Organização de matérias, preparação para mercado de trabalho e desenvolvimento profissional.',
        objetivos: [
            'Organizar matérias universitárias',
            'Preparar para mercado de trabalho',
            'Desenvolver habilidades profissionais',
            'Networking e carreira'
        ],
        tecnicasRecomendadas: ['feynman', 'elaboration', 'interleaving', 'self-explanation', 'dual-coding'],
        cor: '#8b5cf6' // roxo
    },
    concurso: {
        id: 'concurso',
        nome: 'Concurso Público',
        icone: '🏆',
        descricao: 'Planos específicos por concurso, técnicas de estudo para provas e gestão de tempo.',
        objetivos: [
            'Aprovar em concurso específico',
            'Organizar estudos para provas',
            'Gerenciar tempo de estudo',
            'Memorizar conteúdo extenso'
        ],
        tecnicasRecomendadas: ['spaced-repetition', 'active-recall', 'retrieval-practice', 'chunking', 'pomodoro'],
        cor: '#f59e0b' // laranja
    },
    profissional: {
        id: 'profissional',
        nome: 'Profissional/Transição',
        icone: '💼',
        descricao: 'Mudança de carreira, certificações profissionais e aprendizado contínuo.',
        objetivos: [
            'Mudar de carreira',
            'Obter certificações',
            'Aprender novas habilidades',
            'Desenvolvimento profissional contínuo'
        ],
        tecnicasRecomendadas: ['feynman', 'elaboration', 'self-explanation', 'dual-coding', 'active-recall'],
        cor: '#ec4899' // rosa
    }
};

// Função para obter perfil
function getPerfil(id) {
    return perfisUsuario[id];
}

// Função para salvar perfil no localStorage
function salvarPerfil(perfilId) {
    localStorage.setItem('ninjabrain_perfil', perfilId);
}

// Função para obter perfil salvo
function obterPerfilSalvo() {
    return localStorage.getItem('ninjabrain_perfil');
}

// Função para limpar perfil (reset)
function limparPerfil() {
    localStorage.removeItem('ninjabrain_perfil');
}

