# Programación Web — Prácticas

Repositorio de prácticas de la materia **Programación Web** del **ITLA**, que van creciendo conforme avanza el cuatrimestre. Cada carpeta corresponde a una práctica y contiene una página web completa en **HTML + CSS** (sin frameworks, sin build).

| | |
|---|---|
| **Materia** | Programación Web |
| **Institución** | ITLA |
| **Autor** | Franklin Junior Peguero Perez — Matrícula 2025-2010 |

---

## Índice de prácticas

| Práctica | Tema | Contenido | Nivel |
|---|---|---|---|
| [Practica #1](./Practica%20%231/) | Blog / reseña de *The Walking Dead* | HTML semántico + CSS con variables (tema oscuro) | Básico |
| [Practica # 2](./Practica%20%23%202/) | Portafolio personal | HTML semántico + CSS intermedio (grid responsive, gradientes, tipografía externa) | Intermedio |

---

## Evolución del cuatrimestre

- **Práctica #1** sienta la base: estructura semántica del documento, navegación por anclas internas, reset de estilos, variables CSS y un layout de una sola columna con tema oscuro.
- **Práctica #2** da el salto: fuentes externas (Google Fonts), CSS Grid con `auto-fit` para una galería de tarjetas, gradientes, `aspect-ratio`, sombras, `hover` effects, media query para móvil y `scroll-behavior: smooth`.

---

## Practica #1 — Blog "The Walking Dead"

**Objetivo:** practicar HTML semántico y CSS con variables para una página de contenido (blog/reseña).

### Contenido de la página

- **Header** con título y navegación (Sinopsis, Curiosidades, Opinión personal).
- **Sinopsis** de la serie con imagen de portada.
- **Curiosidades** en lista con viñetas personalizadas (`::before`).
- **Opinión personal** del autor.
- **Footer** con datos del autor y botón flotante "volver al principio".

### Estructura de archivos

```
Practica #1/
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

## Practica # 2 — Portafolio personal

**Objetivo:** crear una página personal (sobre mí) aplicando CSS intermedio: grid responsive, gradientes, tipografía externa y efectos de interacción.

### Contenido de la página

- **Header** con título y navegación (Datos Personales, Skills, Proyectos).
- **Datos personales**: foto de perfil circular, biografía y botón para descargar el CV (PDF).
- **Skills / Habilidades técnicas**: chips de Frontend (HTML, CSS, JavaScript) y Backend (Python, Java, C#).
- **Proyectos**: galería de 4 tarjetas — Pirry Manager, Donaway, FlowTrack y StackFlow — cada una con captura, descripción y nota de estado en GitHub.
- **Footer** con datos del autor y botón flotante "volver al principio".

### Estructura de archivos

```
Practica # 2/
├── Index.html
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

### Técnicas utilizadas

- Todo lo de la Práctica #1, más:
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

## Cómo ejecutar los proyectos

No hay dependencias ni herramientas de build. Ambas prácticas son HTML + CSS puros:

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   ```
2. Abre el `Index.html` de la práctica que quieras ver directamente en tu navegador (Chrome, Firefox, Edge...).

---

## Convenciones del repositorio

- Cada práctica vive en su propia carpeta: `Practica #N`.
- Siempre existe un `Index.html` como punto de entrada.
- Los estilos van en una carpeta (`Style/` o `Styles/`) con un solo archivo CSS.
- Los recursos (imágenes, documentos) van en `Resources/`.
- Commits breves en minúscula describiendo la práctica.
