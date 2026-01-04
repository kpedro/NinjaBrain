// Biblioteca de Técnicas de Estudo
const tecnicasEstudo = [
    {
        id: 'pomodoro',
        nome: 'Técnica Pomodoro',
        icone: '⏱️',
        categoria: 'Gestão de Tempo',
        nivel: 'Fundamental',
        descricao: 'Divida seu tempo de estudo em blocos de 25 minutos com pausas de 5 minutos.',
        comoFunciona: [
            '1. Escolha uma tarefa para estudar',
            '2. Configure um timer para 25 minutos',
            '3. Estude focado até o timer tocar',
            '4. Faça uma pausa de 5 minutos',
            '5. Repita 4 vezes, depois faça pausa maior (15-30min)'
        ],
        beneficios: [
            'Aumenta foco e concentração',
            'Reduz fadiga mental',
            'Melhora gestão de tempo',
            'Aumenta produtividade'
        ],
        quandoUsar: 'Ideal para sessões longas de estudo e quando você se distrai facilmente.',
        ciencia: 'Baseada em pesquisas sobre ciclos de atenção e produtividade.'
    },
    {
        id: 'feynman',
        nome: 'Técnica Feynman',
        icone: '🎓',
        categoria: 'Compreensão',
        nivel: 'Intermediário',
        descricao: 'Explique o conteúdo como se estivesse ensinando para uma criança.',
        comoFunciona: [
            '1. Escolha um conceito para estudar',
            '2. Escreva uma explicação simples (como para uma criança)',
            '3. Identifique lacunas no seu conhecimento',
            '4. Revise e simplifique ainda mais',
            '5. Use analogias e exemplos práticos'
        ],
        beneficios: [
            'Identifica o que você realmente entende',
            'Força compreensão profunda',
            'Melhora retenção de longo prazo',
            'Desenvolve habilidades de comunicação'
        ],
        quandoUsar: 'Perfeita para conceitos complexos que você precisa dominar completamente.',
        ciencia: 'Baseada no método de Richard Feynman, físico ganhador do Nobel.'
    },
    {
        id: 'spaced-repetition',
        nome: 'Repetição Espaçada',
        icone: '🔄',
        categoria: 'Memorização',
        nivel: 'Intermediário',
        descricao: 'Revise o conteúdo em intervalos crescentes de tempo.',
        comoFunciona: [
            '1. Estude o conteúdo pela primeira vez',
            '2. Revise após 1 dia',
            '3. Revise após 3 dias',
            '4. Revise após 1 semana',
            '5. Revise após 2 semanas, depois 1 mês'
        ],
        beneficios: [
            'Maximiza retenção de memória',
            'Reduz tempo total de estudo',
            'Previne esquecimento',
            'Eficaz para vocabulário e fatos'
        ],
        quandoUsar: 'Ideal para memorizar informações que precisam ser lembradas por muito tempo.',
        ciencia: 'Baseada na Curva do Esquecimento de Ebbinghaus, comprovada cientificamente.'
    },
    {
        id: 'active-recall',
        nome: 'Recuperação Ativa',
        icone: '🧠',
        categoria: 'Memorização',
        nivel: 'Fundamental',
        descricao: 'Force seu cérebro a recuperar informações sem olhar o material.',
        comoFunciona: [
            '1. Estude o conteúdo normalmente',
            '2. Feche o livro/material',
            '3. Tente recordar o que estudou',
            '4. Escreva ou fale em voz alta',
            '5. Verifique o que esqueceu e revise'
        ],
        beneficios: [
            'Fortalece conexões neurais',
            'Identifica lacunas de conhecimento',
            'Melhora retenção significativamente',
            'Mais eficaz que reler passivamente'
        ],
        quandoUsar: 'Use sempre que quiser memorizar informações importantes.',
        ciencia: 'Pesquisas mostram que é 2-3x mais eficaz que reler passivamente.'
    },
    {
        id: 'mind-mapping',
        nome: 'Mapas Mentais',
        icone: '🗺️',
        categoria: 'Organização',
        nivel: 'Fundamental',
        descricao: 'Crie diagramas visuais conectando conceitos relacionados.',
        comoFunciona: [
            '1. Coloque o tema principal no centro',
            '2. Crie ramos para subtópicos principais',
            '3. Adicione detalhes em sub-ramos',
            '4. Use cores e imagens para destacar',
            '5. Conecte ideias relacionadas'
        ],
        beneficios: [
            'Visualiza relações entre conceitos',
            'Facilita revisão rápida',
            'Melhora compreensão geral',
            'Ajuda na organização mental'
        ],
        quandoUsar: 'Perfeito para organizar grandes quantidades de informação e ver o "quadro geral".',
        ciencia: 'Baseado em pesquisas sobre processamento visual e memória espacial.'
    },
    {
        id: 'interleaving',
        nome: 'Estudo Intercalado',
        icone: '🔀',
        categoria: 'Aprendizado',
        nivel: 'Avançado',
        descricao: 'Alternar entre diferentes tipos de problemas ou tópicos durante o estudo.',
        comoFunciona: [
            '1. Em vez de estudar um tópico por vez',
            '2. Estude múltiplos tópicos na mesma sessão',
            '3. Alterne entre eles regularmente',
            '4. Misture tipos de problemas diferentes',
            '5. Force seu cérebro a distinguir entre conceitos'
        ],
        beneficios: [
            'Melhora capacidade de distinguir conceitos',
            'Aumenta transferência de conhecimento',
            'Previne "overlearning" de um tópico',
            'Melhora performance em provas'
        ],
        quandoUsar: 'Ideal quando você precisa aprender múltiplos conceitos relacionados.',
        ciencia: 'Comprovado em pesquisas sobre aprendizagem e transferência de conhecimento.'
    },
    {
        id: 'elaboration',
        nome: 'Elaboração',
        icone: '💭',
        categoria: 'Compreensão',
        nivel: 'Intermediário',
        descricao: 'Conecte novas informações com conhecimento que você já tem.',
        comoFunciona: [
            '1. Ao aprender algo novo, pergunte "por quê?"',
            '2. Conecte com experiências pessoais',
            '3. Relacione com outros conceitos conhecidos',
            '4. Crie exemplos próprios',
            '5. Explique as conexões em voz alta'
        ],
        beneficios: [
            'Cria conexões significativas',
            'Facilita recuperação de memória',
            'Aumenta compreensão profunda',
            'Torna o aprendizado mais pessoal'
        ],
        quandoUsar: 'Use quando quiser entender profundamente, não apenas memorizar.',
        ciencia: 'Baseada na teoria da elaboração e processamento profundo de informações.'
    },
    {
        id: 'dual-coding',
        nome: 'Codificação Dupla',
        icone: '👁️👂',
        categoria: 'Memorização',
        nivel: 'Intermediário',
        descricao: 'Combine informações verbais com visuais para melhorar a memória.',
        comoFunciona: [
            '1. Leia ou ouça a informação (verbal)',
            '2. Crie uma imagem mental ou desenho',
            '3. Combine palavras com imagens',
            '4. Use diagramas, gráficos, esquemas',
            '5. Revise tanto verbal quanto visualmente'
        ],
        beneficios: [
            'Ativa múltiplas áreas do cérebro',
            'Aumenta retenção de memória',
            'Facilita recuperação de informações',
            'Torna o estudo mais interessante'
        ],
        quandoUsar: 'Perfeito para conceitos abstratos que são difíceis de visualizar.',
        ciencia: 'Baseada na teoria da codificação dupla de Paivio, comprovada cientificamente.'
    },
    {
        id: 'retrieval-practice',
        nome: 'Prática de Recuperação',
        icone: '📝',
        categoria: 'Memorização',
        nivel: 'Fundamental',
        descricao: 'Teste-se regularmente em vez de apenas reler o material.',
        comoFunciona: [
            '1. Estude o conteúdo normalmente',
            '2. Crie perguntas sobre o material',
            '3. Teste-se sem olhar as respostas',
            '4. Verifique o que acertou e errou',
            '5. Foque nas áreas que errou'
        ],
        beneficios: [
            'Identifica lacunas de conhecimento',
            'Fortalece memória de longo prazo',
            'Reduz ansiedade em provas',
            'Mais eficaz que reler'
        ],
        quandoUsar: 'Use regularmente, especialmente antes de provas importantes.',
        ciencia: 'Uma das técnicas mais comprovadas cientificamente para melhorar aprendizado.'
    },
    {
        id: 'chunking',
        nome: 'Agrupamento (Chunking)',
        icone: '🧩',
        categoria: 'Organização',
        nivel: 'Fundamental',
        descricao: 'Divida informações grandes em grupos menores e significativos.',
        comoFunciona: [
            '1. Identifique padrões na informação',
            '2. Agrupe itens relacionados',
            '3. Crie categorias lógicas',
            '4. Memorize os grupos primeiro',
            '5. Depois memorize os detalhes dentro de cada grupo'
        ],
        beneficios: [
            'Aumenta capacidade de memória',
            'Facilita organização mental',
            'Torna informações mais gerenciáveis',
            'Melhora compreensão de padrões'
        ],
        quandoUsar: 'Ideal para memorizar listas longas, números, ou informações complexas.',
        ciencia: 'Baseada na pesquisa sobre capacidade de memória de trabalho (7±2 itens).'
    },
    {
        id: 'self-explanation',
        nome: 'Auto-Explicação',
        icone: '🗣️',
        categoria: 'Compreensão',
        nivel: 'Intermediário',
        descricao: 'Explique para si mesmo o que está aprendendo enquanto estuda.',
        comoFunciona: [
            '1. Enquanto lê, pause regularmente',
            '2. Explique em voz alta o que acabou de ler',
            '3. Pergunte "como isso funciona?" e "por quê?"',
            '4. Conecte com conhecimento prévio',
            '5. Revise suas explicações'
        ],
        beneficios: [
            'Força processamento ativo',
            'Identifica mal-entendidos',
            'Melhora compreensão profunda',
            'Desenvolve pensamento crítico'
        ],
        quandoUsar: 'Use especialmente com material complexo ou conceitos difíceis.',
        ciencia: 'Comprovada em pesquisas sobre aprendizagem autorregulada e metacognição.'
    }
];

// Função para obter técnica por ID
function getTecnica(id) {
    return tecnicasEstudo.find(t => t.id === id);
}

// Função para filtrar técnicas
function filtrarTecnicas(filtro) {
    if (!filtro || filtro === 'todas') {
        return tecnicasEstudo;
    }
    
    if (filtro === 'fundamental') {
        return tecnicasEstudo.filter(t => t.nivel === 'Fundamental');
    }
    
    if (filtro === 'intermediario') {
        return tecnicasEstudo.filter(t => t.nivel === 'Intermediário');
    }
    
    if (filtro === 'avancado') {
        return tecnicasEstudo.filter(t => t.nivel === 'Avançado');
    }
    
    if (filtro.categoria) {
        return tecnicasEstudo.filter(t => t.categoria === filtro.categoria);
    }
    
    return tecnicasEstudo;
}

