# Programación Web — Prácticas

Repositorio de prácticas de la materia **Programación Web** del **ITLA**, que van creciendo conforme avanza el cuatrimestre. Cada carpeta corresponde a una práctica y contiene una página web completa en **HTML, CSS y JavaScript** (sin frameworks, sin build).

| | |
|---|---|
| **Materia** | Programación Web |
| **Institución** | ITLA |
| **Autor** | Franklin Junior Peguero Perez — Matrícula 2025-2010 |

---

## Índice de prácticas

| Práctica | Tema | Contenido | Nivel |
|---|---|---|---|
| [Práctica 1](./practica-1/) | Blog / reseña de *The Walking Dead* | HTML semántico + CSS con variables (tema oscuro) | Básico |
| [Práctica 2](./practica-2/) | Portafolio personal | HTML semántico + CSS intermedio (grid responsive, gradientes, tipografía externa) | Intermedio |
| [Práctica 3](./practica-3/) | Lista de la compra e interactividad del portafolio | JavaScript puro: CRUD en el DOM, orden, contador, modo oscuro y *likes* | Intermedio |
| [Práctica 4](./practica-4/) | Explorador de personajes | `fetch`, `async/await`, búsqueda, paginación y renderizado dinámico con la API de Rick and Morty | Intermedio |

---

## Evolución del cuatrimestre

- **Práctica 1** sienta la base: estructura semántica del documento, navegación por anclas internas, reset de estilos, variables CSS y un layout de una sola columna con tema oscuro.
- **Práctica 2** da el salto: fuentes externas (Google Fonts), CSS Grid con `auto-fit` para una galería de tarjetas, gradientes, `aspect-ratio`, sombras, efectos `hover`, media query para móvil y `scroll-behavior: smooth`.
- **Práctica 3** incorpora JavaScript puro en dos partes: la interactividad del portafolio (modo oscuro, contador de *likes* y biografía expandible) y una lista de la compra completa con operaciones sobre el DOM.
- **Práctica 4** consume una API REST pública con `fetch` y `async/await`, y agrega búsqueda, paginación, estados de carga y manejo de errores.

---

## Práctica 1 — Blog "The Walking Dead"

**Objetivo:** practicar HTML semántico y CSS con variables para una página de contenido (blog/reseña).

### Contenido de la página

- **Header** con título y navegación (Sinopsis, Curiosidades, Opinión personal).
- **Sinopsis** de la serie con imagen de portada.
- **Curiosidades** en lista con viñetas personalizadas (`::before`).
- **Opinión personal** del autor.
- **Footer** con datos del autor y botón flotante "volver al principio".

### Estructura de archivos

```text
practica-1/
├── Index.html
├── Style/
│   └── Style.css
└── Resources/
    └── Img/
        └── twd-portada.jpg
```

### Técnicas utilizadas

- HTML semántico: `header`, `nav`, `main`, `section`, `article`, `footer`.
- Navegación por anclas internas (`#sinopsis`, `#curiosidades`, `#opinion`) y `id="inicio"`.
- Meta tags: `charset`, `viewport`, `description`, `author`.
- Reset universal (`* { margin: 0; padding: 0; box-sizing: border-box; }`).
- Variables CSS en `:root` (colores, radio de borde).
- Tema oscuro con acentos rojos (`--accent: #e63946`).
- Selectores por ID (`#sinopsis`, `#curiosidades`) y pseudo-elementos (`::after`, `::before`).
- Transiciones en enlaces y botón flotante `.back-to-top` (`position: fixed`).
- Entidades HTML (`&middot;`, `&#8593;`).

### Cómo abrirlo

Doble clic en `Index.html` (o ábrelo con click derecho → Abrir con → navegador).

---

## Práctica 2 — Portafolio personal

**Objetivo:** crear una página personal (sobre mí) aplicando CSS intermedio: grid responsive, gradientes, tipografía externa y efectos de interacción.

### Contenido de la página

- **Header** con título y navegación (Datos Personales, Skills, Proyectos).
- **Datos personales**: foto de perfil circular, biografía y botón para descargar el CV (PDF).
- **Skills / Habilidades técnicas**: chips de Frontend (HTML, CSS, JavaScript) y Backend (Python, Java, C#).
- **Proyectos**: galería de 4 tarjetas — Pirry Manager, Donaway, FlowTrack y StackFlow — cada una con captura, descripción y nota de estado en GitHub.
- **Footer** con datos del autor y botón flotante "volver al principio".

### Estructura de archivos

```text
practica-2/
├── Index.html
├── Scripts/
│   ├── BtnLike.js
│   ├── modoOscuro.js
│   └── Ocultar.js
├── Styles/
│   └── styles.css
└── Resources/
    ├── Img/
    │   ├── Foto-perfil-yo.png
    │   ├── Pirry-Manager.JPG
    │   ├── Donaway.JPG
    │   ├── FlowTrack.JPG
    │   └── StackFlow.JPG
    └── document/
        └── CV_Franklin_Junior_Peguero_Perez.pdf
```

Los scripts de la carpeta `Scripts/` se agregaron durante la Práctica 3 para añadir la interactividad del portafolio.

### Técnicas utilizadas

- Todo lo de la Práctica 1, más:
- Google Fonts (Poppins) con `preconnect`.
- `html { scroll-behavior: smooth; scroll-padding-top }` para anclas suaves.
- Header con múltiples `radial-gradient` + `linear-gradient`.
- Variables CSS extendidas (colores, sombras).
- **CSS Grid responsive**: `grid-template-columns: repeat(auto-fit, minmax(320px, 1fr))`.
- Tarjetas de proyecto con `aspect-ratio: 16 / 10`, `object-fit: cover` y `overflow: hidden`.
- Efectos `hover`: `translateY`, `scale(1.08)` en imágenes, cambios de color en chips.
- Botón `.btn` con gradiente y sombra.
- Descarga de archivo con `<a download>`.
- Media query `@media (max-width: 720px)` para móvil.
- BEM-like: clases con `__` y guiones (`.habilidades__lista`, `.tarjeta_proyecto`).

### Cómo abrirlo

Doble clic en `Index.html` (o ábrelo con click derecho → Abrir con → navegador).

---

## Práctica 3 — JavaScript: interactividad y lista de la compra

**Objetivo:** aplicar JavaScript puro para manipular el DOM sin librerías, frameworks ni herramientas de build. La práctica se divide en dos partes.

### Parte 1 — Interactividad del portafolio

Esta parte se desarrolló sobre la misma carpeta de la Práctica 2 (`practica-2/`), reutilizando su HTML y CSS y agregando la carpeta `Scripts/`.

Funcionalidades:

- **Modo oscuro / claro:** botón en el header que alterna el tema y actualiza su propio texto.
- **Contador de "me gusta":** botón con un contador que aumenta en cada clic.
- **Biografía expandible:** botón **"Leer más / Leer menos"** que muestra el texto completo o truncado.

### Parte 2 — Lista de la compra

Aplicación de supermercado que mantiene los productos en memoria y actualiza la lista en pantalla.

Funcionalidades:

- Agregar productos con el botón **Agregar** o la tecla **Enter**.
- Validación de campos vacíos con mensaje temporal.
- Marcar y desmarcar productos como completados con el checkbox o haciendo clic en el nombre.
- Eliminar productos de la lista.
- Ordenar alfabéticamente en sentido **A-Z** o **Z-A**.
- Mover los productos completados al final.
- Contador de productos totales y completados.

### Estructura de archivos

```text
practica-2/
├── Index.html
├── Scripts/
│   ├── BtnLike.js
│   ├── modoOscuro.js
│   └── Ocultar.js
├── Styles/
│   └── styles.css
└── Resources/
    ├── Img/
    └── document/

practica-3/
├── index.html
├── script.js
└── styles.css
```

### Técnicas utilizadas

- **JavaScript básico** (sin librerías):
  - `BtnLike.js`: contador de *likes* con una variable de estado y `addEventListener("click")`.
  - `modoOscuro.js`: alterna la clase `modo-oscuro` en `document.body` con `classList.toggle` y actualiza el texto del botón.
  - `Ocultar.js`: trunca la biografía con `substring` y alterna entre "Leer más" y "Leer menos".
  - `script.js`: arreglo de productos, `filter`, `sort`, `forEach`, `createElement`, `appendChild` y `addEventListener`.
  - Selección de elementos con `getElementById` y actualización del DOM con `textContent` y `classList`.
- **CSS para el modo oscuro:** variables redefinidas en `body.modo-oscuro` y fondos ajustados para tarjetas y chips.
- **Controles en el header:** botones agrupados con Flexbox (`.controles`).
- Carga de los scripts al final del `body` para que el DOM exista antes de ejecutarlos.

### Cómo abrirlo

Abre `practica-2/Index.html` para la interactividad del portafolio o `practica-3/index.html` para la lista de la compra. Los scripts se cargan al final del `body`, así que funcionan directamente sin servidor local.

---

## Práctica 4 — Explorador de personajes

**Objetivo:** consumir una API REST pública y mostrar los datos en pantalla usando únicamente HTML, CSS y JavaScript puro.

### Contenido de la página

- **Buscador** por nombre de personaje.
- **Tarjetas** con imagen, nombre, estado y especie.
- **Paginación** con botones **Anterior** y **Siguiente**.
- **Mensajes de estado:** carga, búsqueda sin resultados y errores de conexión o límite de la API.
- **Diseño responsive** con CSS Grid y tema oscuro.

### Estructura de archivos

```text
practica-4/
├── index.html
├── script.js
└── styles.css
```

### Técnicas utilizadas

- `fetch` con `async/await` y validación de `response.ok`.
- Manejo del código `404` para búsquedas sin resultados.
- Construcción de la URL de búsqueda con `URLSearchParams` (`?name=`).
- Paginación usando directamente `info.prev` e `info.next` de la API.
- Renderizado dinámico con `createElement`, `appendChild` y `replaceChildren`.
- Mensajes accesibles con `aria-live` y control de visibilidad con `hidden`.
- CSS Grid responsive, `aspect-ratio`, variables CSS y media queries.
- Sin frameworks, librerías externas ni dependencias.

### API utilizada

```text
https://rickandmortyapi.com/api/character/
```

### Cómo abrirlo

Doble clic en `index.html`. Si el navegador bloquea `fetch` al abrir el archivo con `file://`, sirve la página con un servidor local:

```bash
python -m http.server 8000
```

Desde la raíz del repositorio, abre:

```text
http://localhost:8000/programacion-web/practica-4/
```

> La API puede responder con `429 Too Many Requests` si se hacen muchas peticiones seguidas. En ese caso, espera un momento y vuelve a intentarlo.

---

## Cómo ejecutar los proyectos

No hay dependencias ni herramientas de build. Las prácticas son HTML + CSS + JavaScript puros:

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   ```
2. Abre el archivo de entrada de la práctica que quieras ver directamente en tu navegador (Chrome, Firefox, Edge...):
   - `practica-1/Index.html`
   - `practica-2/Index.html`
   - `practica-3/index.html`
   - `practica-4/index.html`

Para la Práctica 4 se recomienda usar un servidor local si el navegador restringe las peticiones desde `file://`.

---

## Convenciones del repositorio

- Cada práctica vive en su propia carpeta: `practica-N`.
- Las prácticas 1 y 2 usan `Index.html` como punto de entrada; las prácticas 3 y 4 usan `index.html`.
- Los estilos van en un solo archivo CSS, dentro de `Style/`, `Styles/` o en la raíz de la práctica según corresponda.
- Los scripts van en `Scripts/` cuando la práctica tiene varias funcionalidades y en `script.js` cuando es un solo archivo.
- Los recursos (imágenes, documentos) van en `Resources/`.
- Las prácticas nuevas usan nombres de archivo en minúscula, nombres descriptivos en español y código sin comentarios.
- Commits breves en minúscula describiendo la práctica.
