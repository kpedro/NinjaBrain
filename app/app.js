// Carrega o conteúdo markdown
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

// Sistema de tabs
document.addEventListener('DOMContentLoaded', () => {
    // Carrega markdown
    loadMarkdown();

    // Tab switching
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
            document.getElementById(targetTab).classList.add('active');
        });
    });
});

