const parrafoSobreMi = document.getElementById("texto-sobre-mi");
const botonLeerMas = document.getElementById("btn-leer-mas");


const textoCompleto = parrafoSobreMi.textContent;
const limiteCaracteres = 120;
const textoCorto = textoCompleto.substring(0, limiteCaracteres) + "...";
let textoExpandido = false; 


function mostrarTexto() {
    if (textoExpandido) {
        parrafoSobreMi.textContent = textoCompleto;
        botonLeerMas.textContent = "Leer menos";
    } else {
        parrafoSobreMi.textContent = textoCorto;
        botonLeerMas.textContent = "Leer más";
    }
}

function alternarLeerMas() {
    textoExpandido = !textoExpandido;
    mostrarTexto();
}

mostrarTexto(); 
botonLeerMas.addEventListener("click", alternarLeerMas);