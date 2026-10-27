const botonModo = document.getElementById("btn-modo");

function alternarModoOscuro() {
    const esOscuro = document.body.classList.toggle("modo-oscuro");

    if (esOscuro) {
        botonModo.textContent = "Modo claro";
    } else {
        botonModo.textContent = "Modo oscuro";
    }
}

botonModo.addEventListener("click", alternarModoOscuro);