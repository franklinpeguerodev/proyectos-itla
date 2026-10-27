
let contadorLikes = 0;

const botonLike = document.getElementById("btn-like");
const spanLike = document.getElementById("contador-likes")
function sumarLike() {
    contadorLikes++;
    spanLike.textContent = contadorLikes;
}

botonLike.addEventListener("click", sumarLike);