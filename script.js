function updateClock() {
    const now = new Date();
    document.getElementById('clock').innerText = now.toLocaleTimeString();
}


// Update the clock on page load
updateClock();


document.addEventListener('DOMContentLoaded', () => {
    // Handle clock update
    setInterval(updateClock, 1000);

    // Handle tabs
    const buttons = document.querySelectorAll('.tab-btn');
    const panels = document.querySelectorAll('.panel');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Disable all tabs
            buttons.forEach(b => b.classList.remove('active'));
            panels.forEach(p => p.classList.remove('active'));

            // Enable the target tab
            btn.classList.add('active');
            const targetId = btn.getAttribute('data-target');
            document.getElementById(targetId).classList.add('active');

            // Simulated console log
            console.log(`[SYS] Accessing module: ${targetId.toUpperCase()}... OK`);
        });
    });

    const tooltipBox = document.getElementById('retro-tooltip');
    const triggers = document.querySelectorAll('.tooltip');

    triggers.forEach(trigger => {
        // Mouse enter: Fill and display
        trigger.addEventListener('mouseenter', () => {
            const text = trigger.getAttribute('data-desc');
            tooltipBox.innerText = text;
            tooltipBox.classList.remove('hidden');
        });

        // Mouse move: The box follows the mouse
        trigger.addEventListener('mousemove', (e) => {
            // Offset by 15px to avoid hiding the cursor
            const x = e.clientX + 15;
            const y = e.clientY + 15;
            
            tooltipBox.style.left = x + 'px';
            tooltipBox.style.top = y + 'px';
        });

        // Mouse leave: Hide
        trigger.addEventListener('mouseleave', () => {
            tooltipBox.classList.add('hidden');
        });
    });

    // "Easter egg"
    console.log("%c SANTA PROTOCOL INITIATED ", "background: #ff0055; color: white; font-size: 20px;");
});

