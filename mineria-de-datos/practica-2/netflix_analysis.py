import os

import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PyQt5 import QtCore, QtGui, QtWidgets


CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "netflix_titles.csv")
STYLE = """
* { font-family: "Segoe UI", Arial, sans-serif; }
QMainWindow { background: #f4f6fa; }
QTabWidget::pane { border: 0; background: white; border-radius: 12px; margin: 8px; }
QTabBar::tab { background: #e8ecf3; color: #2b3a55; padding: 15px 30px; margin: 4px 4px 0 4px;
    min-width: 180px; min-height: 24px; border-top-left-radius: 10px; border-top-right-radius: 10px;
    font: 600 14px "Segoe UI"; }
QTabBar::tab:selected { background: white; color: #1f8a5a; border-bottom: 2px solid #1f8a5a; }
QTabBar::tab:hover:!selected { background: #dde3ee; }
QLabel#Header { font-size: 22px; font-weight: 700; color: #1f8a5a; padding: 4px 0 10px; }
QLabel#Subtitle { color: #6b7280; font-size: 12px; padding-bottom: 8px; }
QLabel#SectionTitle { color: #1f2937; font-size: 14px; font-weight: 600; padding: 6px 2px; }
QTableWidget { background: white; alternate-background-color: #f1f5f9; gridline-color: #e5e9f0;
    border: 1px solid #e5e9f0; border-radius: 10px; font: 11px "Segoe UI"; selection-background-color: #1f8a5a; }
QHeaderView::section { background: #1f8a5a; color: white; padding: 9px; border: 0; font-weight: 600; }
QGroupBox { background: white; border: 1px solid #e5e9f0; border-radius: 12px;
    margin-top: 14px; padding: 16px 14px 14px; font-weight: 600; color: #1f2937; }
QGroupBox::title { subcontrol-origin: margin; left: 14px; padding: 0 6px; color: #1f8a5a; }
"""


class NetflixApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Análisis del catálogo de Netflix")
        self.resize(1450, 850)
        self.setStyleSheet(STYLE)
        self.df_raw = pd.read_csv(CSV_PATH)
        self.na_before = int(self.df_raw.isna().sum().sum())
        self.df = self.df_raw.fillna(0)

        root = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(root)
        layout.setContentsMargins(16, 14, 16, 14)
        header = QtWidgets.QLabel("Análisis del catálogo de Netflix")
        header.setObjectName("Header")
        subtitle = QtWidgets.QLabel("Minería de datos  -  Práctica 2")
        subtitle.setObjectName("Subtitle")
        layout.addWidget(header)
        layout.addWidget(subtitle)

        tabs = QtWidgets.QTabWidget()
        tabs.setDocumentMode(True)
        tabs.tabBar().setExpanding(True)
        tabs.addTab(self._info_tab(), "Resumen y estadísticos")
        tabs.addTab(self._table_tab(self.df.head(10), "Primeros 10 registros"), "Primeros 10")
        tabs.addTab(self._table_tab(self.df.tail(15), "Últimos 15 registros"), "Últimos 15")
        tabs.addTab(self._chart_tab(), "Películas vs. series")
        layout.addWidget(tabs)
        self.setCentralWidget(root)

    def _info_tab(self):
        w = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(w)
        layout.setContentsMargins(8, 8, 8, 8)
        rows, cols = self.df.shape
        dimensions = QtWidgets.QGroupBox("Dimensiones y limpieza")
        box = QtWidgets.QHBoxLayout(dimensions)
        for label, value in (("Registros", f"{rows:,}"), ("Columnas", str(cols)),
                             ("Valores NA (antes)", f"{self.na_before:,}"),
                             ("Valores NA (después)", str(int(self.df.isna().sum().sum())))):
            card = QtWidgets.QFrame()
            card.setStyleSheet("QFrame { background:#f8fafc; border:1px solid #e5e9f0; border-radius:8px; }")
            card_layout = QtWidgets.QVBoxLayout(card)
            card_layout.setContentsMargins(14, 10, 14, 10)
            card_layout.setSpacing(3)
            caption = QtWidgets.QLabel(label)
            caption.setStyleSheet("color:#6b7280; border:0; font-size:11px; font-weight:600;")
            number = QtWidgets.QLabel(value)
            number.setStyleSheet("color:#111827; border:0; font-size:21px; font-weight:700;")
            card_layout.addWidget(caption)
            card_layout.addWidget(number)
            box.addWidget(card, 1)
        layout.addWidget(dimensions)

        stats = self.df.describe(include="all").transpose().rename_axis("columna").reset_index()
        section = QtWidgets.QLabel("Estadísticos básicos · columnas numéricas y categóricas")
        section.setObjectName("SectionTitle")
        layout.addWidget(section)
        layout.addWidget(self._table(stats))
        return w

    def _table(self, data):
        table = QtWidgets.QTableWidget(len(data), len(data.columns))
        table.setHorizontalHeaderLabels([str(c) for c in data.columns])
        table.setAlternatingRowColors(True)
        table.verticalHeader().setVisible(False)
        table.verticalHeader().setDefaultSectionSize(30)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        table.setWordWrap(False)

        table.setTextElideMode(QtCore.Qt.ElideNone)
        for r, row in enumerate(data.itertuples(index=False, name=None)):
            for c, value in enumerate(row):
                # Las celdas NaN se muestran como 0 en todas las tablas.
                # Esto afecta principalmente al resumen, donde describe() produce
                # NaN para estadísticas no aplicables a columnas de texto.
                text = "0" if pd.isna(value) else (f"{value:.2f}" if isinstance(value, float) else str(value))
                item = QtWidgets.QTableWidgetItem(text)
                item.setToolTip(text)
                item.setFont(QtGui.QFont("Segoe UI", 10))
                table.setItem(r, c, item)
        table.resizeColumnsToContents()
        table.horizontalHeader().setMinimumSectionSize(85)
        table.horizontalHeader().setStretchLastSection(True)
        if "title" in data.columns:
            title_column = data.columns.get_loc("title")
            title_width = max(
                QtGui.QFontMetrics(table.font()).horizontalAdvance(str(value)) + 28
                for value in data["title"]
            )

            table.setColumnWidth(title_column, min(max(title_width, 520), 900))
        table.setMinimumWidth(400)
        return table

    def _table_tab(self, data, title):
        w = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(w)
        layout.setContentsMargins(8, 8, 8, 8)
        header = QtWidgets.QLabel(title)
        header.setObjectName("Header")
        subtitle = QtWidgets.QLabel(f"{len(data)} filas × {len(data.columns)} columnas — valores faltantes reemplazados por 0")
        subtitle.setObjectName("Subtitle")
        layout.addWidget(header)
        layout.addWidget(subtitle)
        layout.addWidget(self._table(data.reset_index(drop=True)))
        return w

    def _chart_tab(self):
        w = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(w)
        layout.setContentsMargins(8, 8, 8, 8)
        header = QtWidgets.QLabel("Películas vs. series por año de lanzamiento")
        header.setObjectName("Header")
        subtitle = QtWidgets.QLabel("Conteo de títulos estrenados entre 2010 y 2021, inclusive")
        subtitle.setObjectName("Subtitle")
        layout.addWidget(header)
        layout.addWidget(subtitle)

        years = list(range(2010, 2022))
        subset = self.df[self.df["release_year"].between(2010, 2021)].copy()
        counts = subset.groupby(["release_year", "type"]).size().unstack(fill_value=0)
        counts = counts.reindex(index=years, columns=["Movie", "TV Show"], fill_value=0)
        counts.columns = ["Películas", "Series"]

        fig, ax = plt.subplots(figsize=(10, 5.5))
        fig.patch.set_facecolor("white")
        counts.plot(kind="bar", ax=ax, color=["#1f8a5a", "#2b6cb0"], width=0.78)
        ax.set_xlabel("Año de lanzamiento", color="#374151")
        ax.set_ylabel("Cantidad de títulos", color="#374151")
        ax.set_title("Cantidad de películas y series por año (2010–2021)", color="#111827", pad=14)
        ax.set_xticklabels(years, rotation=0)
        ax.legend(frameon=False)
        ax.grid(axis="y", alpha=0.25, linestyle="--")
        ax.set_axisbelow(True)
        ax.set_facecolor("#f8fafc")
        for spine in ax.spines.values():
            spine.set_color("#e5e9f0")
        fig.tight_layout()
        canvas = FigureCanvasQTAgg(fig)
        layout.addWidget(canvas)
        return w


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setFont(QtGui.QFont("Segoe UI", 10))
    window = NetflixApp()
    window.show()
    app.exec_()
