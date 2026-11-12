"use strict";

const API_URL = "https://rickandmortyapi.com/api/character/";

const formulario = document.getElementById("formBusqueda");
const inputBusqueda = document.getElementById("inputBusqueda");
const mensaje = document.getElementById("mensaje");
const contenedor = document.getElementById("personajes");
const paginacion = document.getElementById("paginacion");
const btnAnterior = document.getElementById("btnAnterior");
const btnSiguiente = document.getElementById("btnSiguiente");
const indicadorPagina = document.getElementById("indicadorPagina");

let busqueda = "";
let pagina = 1;
let urlAnterior = null;
let urlSiguiente = null;

function mostrarMensaje(texto, tipo = "") {
    mensaje.textContent = texto;
    mensaje.className = "mensaje";

    if (tipo !== "") {
        mensaje.classList.add(`mensaje--${tipo}`);
    }
}

function crearUrl() {
    const parametros = new URLSearchParams();

    if (busqueda !== "") {
        parametros.set("name", busqueda);
    }

    const cadena = parametros.toString();
    return cadena === "" ? API_URL : `${API_URL}?${cadena}`;
}

function crearTarjeta(personaje) {
    const tarjeta = document.createElement("article");
    tarjeta.className = "personaje";

    const contenedorImagen = document.createElement("div");
    contenedorImagen.className = "personaje__imagen-contenedor";

    const imagen = document.createElement("img");
    imagen.className = "personaje__imagen";
    imagen.src = personaje.image;
    imagen.alt = `Imagen de ${personaje.name}`;
    imagen.width = 300;
    imagen.height = 300;

    contenedorImagen.appendChild(imagen);

    const contenido = document.createElement("div");
    contenido.className = "personaje__contenido";

    const nombre = document.createElement("h2");
    nombre.className = "personaje__nombre";
    nombre.textContent = personaje.name;

    const meta = document.createElement("div");
    meta.className = "personaje__meta";

    const estadoPersonaje = document.createElement("span");
    estadoPersonaje.className = "personaje__estado";
    estadoPersonaje.textContent = personaje.status || "unknown";

    const especie = document.createElement("span");
    especie.className = "personaje__especie";
    especie.textContent = personaje.species || "Especie desconocida";

    meta.append(estadoPersonaje, especie);
    contenido.append(nombre, meta);
    tarjeta.append(contenedorImagen, contenido);

    return tarjeta;
}

function renderizarPersonajes(personajes) {
    contenedor.replaceChildren();

    personajes.forEach(function (personaje) {
        contenedor.appendChild(crearTarjeta(personaje));
    });
}

async function cargarPersonajes(url, numeroPagina) {
    pagina = numeroPagina;

    contenedor.replaceChildren();
    paginacion.hidden = true;
    mostrarMensaje("Cargando...", "cargando");

    try {
        const respuesta = await fetch(url);

        if (respuesta.status === 404) {
            urlAnterior = null;
            urlSiguiente = null;
            btnAnterior.disabled = true;
            btnSiguiente.disabled = true;
            mostrarMensaje("No se encontraron personajes.", "error");
            return;
        }

        if (!respuesta.ok) {
            throw new Error(`Error HTTP ${respuesta.status}`);
        }

        const datos = await respuesta.json();

        renderizarPersonajes(datos.results);

        urlAnterior = datos.info.prev;
        urlSiguiente = datos.info.next;

        btnAnterior.disabled = urlAnterior === null;
        btnSiguiente.disabled = urlSiguiente === null;

        indicadorPagina.textContent = `Página ${pagina} de ${datos.info.pages}`;
        paginacion.hidden = false;

        mostrarMensaje(`Mostrando ${datos.results.length} de ${datos.info.count} personajes.`, "info");
    } catch (error) {
        urlAnterior = null;
        urlSiguiente = null;
        btnAnterior.disabled = true;
        btnSiguiente.disabled = true;

        if (error.message.includes("429")) {
            mostrarMensaje("La API está limitando las solicitudes. Espera un minuto y vuelve a intentarlo.", "error");
        } else if (error.message.startsWith("Error HTTP")) {
            mostrarMensaje("La API respondió con un error. Inténtalo de nuevo en unos segundos.", "error");
        } else {
            mostrarMensaje("No se pudo conectar con la API. Revisa tu conexión o usa un servidor local.", "error");
        }
    }
}

formulario.addEventListener("submit", function (evento) {
    evento.preventDefault();

    busqueda = inputBusqueda.value.trim();
    pagina = 1;

    cargarPersonajes(crearUrl(), 1);
});

btnAnterior.addEventListener("click", function () {
    if (urlAnterior !== null) {
        cargarPersonajes(urlAnterior, pagina - 1);
    }
});

btnSiguiente.addEventListener("click", function () {
    if (urlSiguiente !== null) {
        cargarPersonajes(urlSiguiente, pagina + 1);
    }
});

cargarPersonajes(crearUrl(), 1);
