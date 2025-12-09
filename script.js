document.addEventListener('DOMContentLoaded', () => {
    // Gestion de l'horloge
    setInterval(() => {
        const now = new Date();
        document.getElementById('clock').innerText = now.toLocaleTimeString();
    }, 1000);

    // Gestion des onglets
    const buttons = document.querySelectorAll('.tab-btn');
    const panels = document.querySelectorAll('.panel');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Désactiver tout
            buttons.forEach(b => b.classList.remove('active'));
            panels.forEach(p => p.classList.remove('active'));

            // Activer la cible
            btn.classList.add('active');
            const targetId = btn.getAttribute('data-target');
            document.getElementById(targetId).classList.add('active');

            // Son simulé (console)
            console.log(`[SYS] Accessing module: ${targetId.toUpperCase()}... OK`);
        });
    });

    // Petit "Easter Egg" au chargement
    console.log("%c SANTA PROTOCOL INITIATED ", "background: #ff0055; color: white; font-size: 20px;");
});