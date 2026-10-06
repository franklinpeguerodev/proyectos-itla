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

## Convenciones del repositorio

- Cada práctica vive en su propia carpeta: `practica-N`.
- Los datos fuente necesarios para ejecutar cada práctica se guardan junto al código.
- Los archivos generados, entornos virtuales y cachés locales no se incluyen en Git.
