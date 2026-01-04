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

  if (!message || !message.trim()) {
    return res.status(400).json({ error: 'Mensagem é obrigatória' });
  }

  const apiKey = process.env.GEMINI_API_KEY;

  if (!apiKey) {
    console.error('GEMINI_API_KEY não configurada');
    return res.status(500).json({ error: 'API key não configurada no servidor' });
  }

  try {
    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash-exp' });

    // Contextos baseados no perfil
    const contextos = {
      fundamental: `Você é o NinjaBrain, assistente educacional para estudantes do Ensino Fundamental.
Seja claro, use exemplos simples e seja encorajador.
Ajude com organização de estudos, técnicas de memorização e preparação para provas escolares.`,
      
      medio: `Você é o NinjaBrain, assistente educacional para estudantes do Ensino Médio.
Foque em preparação para ENEM/Vestibular, técnicas eficientes de estudo e priorização.
Seja direto e focado em resultados práticos.`,
      
      superior: `Você é o NinjaBrain, assistente educacional para estudantes universitários.
Foque em organização acadêmica, preparação para mercado de trabalho e desenvolvimento profissional.
Ajude a conectar teoria com prática.`,
      
      concurso: `Você é o NinjaBrain, assistente especializado em concursos públicos.
Seja direto, técnico e focado em aprovação.
Use a regra 80/20: 20% do conteúdo gera 80% das questões.
Priorize o que realmente cai na prova.`,
      
      profissional: `Você é o NinjaBrain, assistente para profissionais em transição de carreira.
Foque em aprendizado acelerado, desenvolvimento de habilidades práticas e preparação para o mercado.
Seja objetivo e orientado a resultados.`
    };

    const contexto = contextos[perfil] || contextos.concurso;

    const prompt = `${contexto}

Instruções:
- Responda de forma direta e objetiva
- Use exemplos práticos quando possível
- Seja encorajador e motivador
- Foque em resultados e eficiência
- Se não souber algo, seja honesto

Pergunta do estudante: ${message.trim()}

Responda de forma útil e prática:`;

    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();

    return res.status(200).json({ 
      resposta: text,
      sucesso: true 
    });

  } catch (error) {
    console.error('Erro na API Gemini:', error);
    
    // Mensagens de erro mais amigáveis
    let mensagemErro = 'Desculpe, ocorreu um erro ao processar sua mensagem.';
    
    if (error.message?.includes('API_KEY')) {
      mensagemErro = 'Erro de configuração da API. Entre em contato com o suporte.';
    } else if (error.message?.includes('quota') || error.message?.includes('limit')) {
      mensagemErro = 'Limite de requisições atingido. Tente novamente em alguns minutos.';
    }
    
    return res.status(500).json({ 
      error: mensagemErro,
      detalhes: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
};

