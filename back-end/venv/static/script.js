// Selecione todos os campos de entrada (input[type="text"])
const inputs = document.querySelectorAll('input[type="text"]');

// Adiciona eventos de "focus" e "blur" a cada campo de entrada
inputs.forEach(input => {
    input.addEventListener('focus', () => {
        input.style.width = '120%'; // Aumenta a largura do campo quando ele é clicado
        input.style.height = '40px'; // Aumenta a altura do campo
    });

    input.addEventListener('blur', () => {
        input.style.width = '100%'; // Restaura a largura do campo quando perde o foco
        input.style.height = 'auto'; // Restaura a altura do campo
    });
});
