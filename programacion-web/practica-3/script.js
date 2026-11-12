
let productos = [];

let direccionOrden = "asc";


const inputProducto = document.getElementById("inputProducto");
const btnAgregar = document.getElementById("btnAgregar");
const btnOrdenar = document.getElementById("btnOrdenar");
const btnMoverCompletados = document.getElementById("btnMoverCompletados");
const listaProductos = document.getElementById("listaProductos");
const mensaje = document.getElementById("mensaje");
const contador = document.getElementById("contador");


function mostrarMensaje(texto, esOk) {
    mensaje.textContent = texto;
    if (esOk) {
        mensaje.classList.add("ok");
    } else {
        mensaje.classList.remove("ok");
    }
   
    setTimeout(function () {
        mensaje.textContent = "";
        mensaje.classList.remove("ok");
    }, 2000);
}


function esTextoValido(texto) {
    if (texto.trim() === "") {
        return false;
    }
    return true;
}


function agregarProducto() {
    const nombre = inputProducto.value;

   
    if (!esTextoValido(nombre)) {
        mostrarMensaje("No se puede agregar un producto vacío.", false);
        return;
    }

    productos.push({ nombre: nombre.trim(), completado: false });

    inputProducto.value = "";
    inputProducto.focus();

    mostrarMensaje("Producto agregado correctamente.", true);

    
    renderLista();
}


function alternarCompletado(indice) {
    if (indice < 0 || indice >= productos.length) {
        return;
    }
    productos[indice].completado = !productos[indice].completado;
    renderLista();
}


function eliminarProducto(indice) {
    productos = productos.filter(function (_, i) {
        return i !== indice;
    });
    renderLista();
}


function ordenarLista() {
    productos.sort(function (a, b) {
        const nombreA = a.nombre.toLowerCase();
        const nombreB = b.nombre.toLowerCase();

        if (direccionOrden === "asc") {
            if (nombreA < nombreB) return -1;
            if (nombreA > nombreB) return 1;
            return 0;
        } else {
            if (nombreA > nombreB) return -1;
            if (nombreA < nombreB) return 1;
            return 0;
        }
    });


    direccionOrden = direccionOrden === "asc" ? "desc" : "asc";

   
    if (direccionOrden === "asc") {
        btnOrdenar.textContent = "Ordenar A-Z";
    } else {
        btnOrdenar.textContent = "Ordenar Z-A";
    }

    renderLista();
}


function moverCompletadosAlFinal() {
    const pendientes = productos.filter(function (p) {
        return !p.completado;
    });
    const completados = productos.filter(function (p) {
        return p.completado;
    });
    productos = pendientes.concat(completados);
    renderLista();
}


function actualizarContador() {
    const total = productos.length;
    const completados = productos.filter(function (p) {
        return p.completado;
    }).length;
    contador.textContent = total + " producto(s) - " + completados + " completado(s)";
}


function renderLista() {
   
    listaProductos.innerHTML = "";

    
    productos.forEach(function (producto, indice) {
        
        const li = document.createElement("li");
        li.className = "item-producto";
        if (producto.completado) {
            li.classList.add("completado");
        }


        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.className = "checkbox-producto";
        checkbox.checked = producto.completado;
    
        checkbox.addEventListener("change", function () {
            alternarCompletado(indice);
        });

        
        const spanNombre = document.createElement("span");
        spanNombre.className = "nombre-producto";
        spanNombre.textContent = producto.nombre;
        
        spanNombre.addEventListener("click", function () {
            alternarCompletado(indice);
        });

       
        const btnEliminar = document.createElement("button");
        btnEliminar.className = "btn btn-eliminar";
        btnEliminar.type = "button";
        btnEliminar.textContent = "Eliminar";
        btnEliminar.addEventListener("click", function () {
            eliminarProducto(indice);
        });

        
        li.appendChild(checkbox);
        li.appendChild(spanNombre);
        li.appendChild(btnEliminar);

        listaProductos.appendChild(li);
    });

    actualizarContador();
}




btnAgregar.addEventListener("click", agregarProducto);


inputProducto.addEventListener("keydown", function (evento) {
    if (evento.key === "Enter") {
        agregarProducto();
    }
});


btnOrdenar.addEventListener("click", ordenarLista);


btnMoverCompletados.addEventListener("click", moverCompletadosAlFinal);


renderLista();
