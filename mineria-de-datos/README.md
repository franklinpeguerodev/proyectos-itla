# Minería de Datos — Prácticas

Repositorio de prácticas de la materia **Minería de Datos** del **ITLA**, organizadas por número y tema. La primera práctica trabaja con un conjunto de datos de aguacates y presenta sus estadísticas y visualizaciones en una aplicación de escritorio hecha con Python.

| | |
|---|---|
| **Materia** | Minería de Datos |
| **Institución** | ITLA |
| **Autor** | Franklin Junior Peguero Perez — Matrícula 2025-2010 |

---

## Índice de prácticas

| Práctica | Tema | Contenido | Nivel |
|---|---|---|---|
| [Práctica 1](./practica-1/) | Análisis de aguacates | Exploración de datos, tablas resumen y gráfico de dispersión con Python | Básico |
| [Práctica 2](./practica-2/) | Catálogo de Netflix | Estadísticos básicos y comparación anual de películas y series | Básico |

---

## Práctica 1 — Análisis del dataset de aguacates

**Objetivo:** explorar el dataset `avocado.csv` y presentar información descriptiva de sus precios, regiones, años y tipos de aguacate en una interfaz gráfica.

### Contenido de la aplicación

- Resumen con dimensiones del dataset y estadísticas del precio promedio.
- Vistas tabulares de los primeros 100 y los últimos 20 registros.
- Gráfico de dispersión que relaciona el año con `AveragePrice` para California, New York y Chicago.
- Interfaz de escritorio con pestañas, construida con PyQt5 e integrada con Matplotlib.

### Estructura de archivos

```
practica-1/
├── .gitignore
├── avocado.csv
├── avocado_analysis.py
└── pyproject.toml
```

Al ejecutar la aplicación, Matplotlib genera `scatter_avocado.png` en esta misma carpeta. El archivo que ya está en el repositorio se conserva; las nuevas generaciones quedan ignoradas por el `.gitignore` de la práctica.

### Tecnologías utilizadas

- Python.
- Pandas para leer y consultar el archivo CSV.
- Matplotlib para crear el gráfico de dispersión.
- PyQt5 para la interfaz gráfica de escritorio.
- `pyproject.toml` contiene opciones de configuración para mypy.

### Cómo ejecutar la práctica

Se requiere Python y las dependencias `pandas`, `matplotlib` y `PyQt5`. Desde la carpeta `practica-1`, instala las dependencias y ejecuta el script:

```bash
python -m pip install pandas matplotlib PyQt5
python avocado_analysis.py
```

El archivo `avocado.csv` debe permanecer junto al script; la aplicación lo carga desde la misma carpeta.

---

## Práctica 2 — Análisis del catálogo de Netflix

**Objetivo:** explorar `netflix_titles.csv`, completar los datos faltantes con cero y comparar la cantidad de películas y series por año de lanzamiento.

### Contenido de la aplicación

- Resumen con el tamaño del dataset y la cantidad de valores NA restantes tras la limpieza.
- Estadísticos descriptivos de las columnas numéricas y categóricas.
- Vistas tabulares de los primeros 10 y los últimos 15 registros.
- Gráfico de barras agrupadas para películas y series entre 2010 y 2021, inclusive.
- Interfaz de escritorio construida con PyQt5 e integrada con Matplotlib.

### Estructura

```
practica-2/
├── netflix_titles.csv
└── netflix_analysis.py
```

### Cómo ejecutar la práctica

Se requiere Python y las dependencias `pandas`, `matplotlib` y `PyQt5`. Desde la carpeta `practica-2`, instala las dependencias y ejecuta:

```bash
python -m pip install pandas matplotlib PyQt5
python netflix_analysis.py
```

El CSV debe permanecer junto al script. El gráfico se basa en `release_year`; si un año no tiene títulos en el dataset, se muestra con conteo cero.

---

## Convenciones del repositorio

- Cada práctica vive en su propia carpeta: `practica-N`.
- Los datos fuente necesarios para ejecutar cada práctica se guardan junto al código.
- Los archivos generados, entornos virtuales y cachés locales no se incluyen en Git.
