import os
import pandas as pd
import matplotlib

matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PyQt5 import QtCore, QtGui, QtWidgets

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "avocado.csv")
REGIONES = ["California", "NewYork", "Chicago"]

STYLE = """
* { font-family: "Segoe UI", Arial, sans-serif; }
QMainWindow { background: #f4f6fa; }
QTabWidget::pane {
    border: 0;
    background: #ffffff;
    border-radius: 12px;
    margin: 8px;
}
QTabBar {
    font-family: "Segoe UI", Arial, sans-serif;
}
QTabBar::tab {
    background: #e8ecf3;
    color: #2b3a55;
    padding: 12px 26px;
    margin: 4px 4px 0 4px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    font: 600 13px "Segoe UI", Arial, sans-serif;
    min-width: 110px;
    min-height: 22px;
}
QTabBar::tab:selected {
    background: #ffffff;
    color: #1f8a5a;
    border-bottom: 2px solid #1f8a5a;
}
QTabBar::tab:hover { background: #dde3ee; }
QTabBar::tab:!selected { color: #2b3a55; }
QLabel#Header {
    font-size: 22px;
    font-weight: 700;
    color: #1f8a5a;
    padding: 4px 0 10px 0;
}
QLabel#Subtitle {
    color: #6b7280;
    font-size: 12px;
    padding-bottom: 8px;
}
QGroupBox {
    background: #ffffff;
    border: 1px solid #e5e9f0;
    border-radius: 12px;
    margin-top: 14px;
    padding: 16px 14px 14px 14px;
    font-weight: 600;
    color: #1f2937;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 14px;
    padding: 0 6px;
    color: #1f8a5a;
}
QFrame#Card {
    background: #f8fafc;
    border: 1px solid #e5e9f0;
    border-radius: 10px;
}
QLabel#CardTitle {
    color: #6b7280;
    font-size: 11px;
    font-weight: 600;
}
QLabel#CardValue {
    color: #111827;
    font-size: 22px;
    font-weight: 700;
}
QTableWidget {
    background: #ffffff;
    alternate-background-color: #f1f5f9;
    gridline-color: #e5e9f0;
    border: 1px solid #e5e9f0;
    border-radius: 10px;
    selection-background-color: #1f8a5a;
    selection-color: white;
    font: 12px "Segoe UI", Arial, sans-serif;
}
QTableWidget::item {
    padding: 6px 10px;
    border: 0;
    color: #1f2937;
}
QTableWidget::item:selected {
    background: #1f8a5a;
    color: white;
}
QHeaderView {
    background: #1f8a5a;
}
QHeaderView::section {
    background: #1f8a5a;
    color: white;
    padding: 10px 12px;
    border: 0;
    font: 600 12px "Segoe UI", Arial, sans-serif;
    min-height: 28px;
}
QHeaderView::section:hover { background: #16724a; }
QScrollBar:vertical {
    background: transparent; width: 10px; margin: 4px 2px;
}
QScrollBar::handle:vertical {
    background: #c7cfdb; border-radius: 5px; min-height: 24px;
}
QScrollBar::handle:vertical:hover { background: #a9b3c5; }
QScrollBar:horizontal {
    background: transparent; height: 10px; margin: 2px 4px;
}
QScrollBar::handle:horizontal {
    background: #c7cfdb; border-radius: 5px; min-width: 24px;
}
QScrollBar::handle:horizontal:hover { background: #a9b3c5; }
QScrollBar::add-line, QScrollBar::sub-line { background: transparent; height: 0; width: 0; }
"""


class AvocadoApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analisis de Aguacate")
        self.resize(1150, 740)
        self.setStyleSheet(STYLE)

        self.df = pd.read_csv(CSV_PATH)

        root = QtWidgets.QWidget()
        root_layout = QtWidgets.QVBoxLayout(root)
        root_layout.setContentsMargins(16, 14, 16, 14)
        root_layout.setSpacing(6)

        header = QtWidgets.QLabel("Analisis del dataset de Aguacates")
        header.setObjectName("Header")
        subtitle = QtWidgets.QLabel("Mineria de datos  -  C5")
        subtitle.setObjectName("Subtitle")
        root_layout.addWidget(header)
        root_layout.addWidget(subtitle)

        tabs = QtWidgets.QTabWidget()
        tabs.setDocumentMode(True)
        root_layout.addWidget(tabs)

        tabs.addTab(self._build_info_tab(), "Informacion")
        tabs.addTab(self._build_table_tab(self.df.head(100), "Primeros 100 registros"), "Primeros 100")
        tabs.addTab(self._build_table_tab(self.df.tail(20), "Ultimos 20 registros"), "Ultimos 20")
        tabs.addTab(self._build_plot_tab(), "Grafico")

        self.setCentralWidget(root)

    def _card(self, title, value):
        frame = QtWidgets.QFrame()
        frame.setObjectName("Card")
        v = QtWidgets.QVBoxLayout(frame)
        v.setContentsMargins(14, 10, 14, 10)
        v.setSpacing(2)
        t = QtWidgets.QLabel(title)
        t.setObjectName("CardTitle")
        val = QtWidgets.QLabel(value)
        val.setObjectName("CardValue")
        v.addWidget(t)
        v.addWidget(val)
        return frame

    def _build_info_tab(self):
        w = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(w)
        layout.setContentsMargins(8, 8, 8, 8)

        filas, columnas = self.df.shape
        precio = self.df["AveragePrice"]

        gb_dims = QtWidgets.QGroupBox("1) Dimensiones del dataset")
        g1 = QtWidgets.QHBoxLayout(gb_dims)
        g1.addWidget(self._card("Filas", f"{filas:,}"))
        g1.addWidget(self._card("Columnas", f"{columnas}"))
        g1.addStretch(1)
        layout.addWidget(gb_dims)

        gb_price = QtWidgets.QGroupBox("4) Precio (AveragePrice)")
        g2 = QtWidgets.QHBoxLayout(gb_price)
        g2.addWidget(self._card("Minimo", f"${precio.min():.2f}"))
        g2.addWidget(self._card("Maximo", f"${precio.max():.2f}"))
        g2.addWidget(self._card("Promedio", f"${precio.mean():.4f}"))
        g2.addStretch(1)
        layout.addWidget(gb_price)

        gb_meta = QtWidgets.QGroupBox("Detalles del dataset")
        g3 = QtWidgets.QVBoxLayout(gb_meta)
        meta = QtWidgets.QLabel(
            f"Archivo: avocado.csv\n"
            f"Regiones unicas: {self.df['region'].nunique()}\n"
            f"Anios cubiertos: {self.df['year'].min()} - {self.df['year'].max()}\n"
            f"Tipos: {', '.join(sorted(self.df['type'].unique()))}"
        )
        meta.setStyleSheet("color:#374151; font-size:12px; line-height:1.6;")
        g3.addWidget(meta)
        layout.addWidget(gb_meta)
        layout.addStretch(1)

        return w

    def _build_table_tab(self, data, title):
        w = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(w)
        layout.setContentsMargins(8, 8, 8, 8)

        header = QtWidgets.QLabel(title)
        header.setObjectName("Header")
        sub = QtWidgets.QLabel(f"{len(data)} filas x {len(data.columns)} columnas")
        sub.setObjectName("Subtitle")
        layout.addWidget(header)
        layout.addWidget(sub)

        table = QtWidgets.QTableWidget()
        cols = list(data.columns)
        table.setColumnCount(len(cols))
        table.setRowCount(len(data))
        table.setHorizontalHeaderLabels(cols)
        table.setAlternatingRowColors(True)
        table.verticalHeader().setVisible(False)
        table.verticalHeader().setDefaultSectionSize(32)
        table.horizontalHeader().setMinimumSectionSize(90)
        table.setShowGrid(False)
        table.setWordWrap(False)
        table.setTextElideMode(QtCore.Qt.ElideRight)

        header_font = QtGui.QFont("Segoe UI", 11, QtGui.QFont.Bold)
        table.horizontalHeader().setFont(header_font)

        for r, (_, row) in enumerate(data.iterrows()):
            for c, col in enumerate(cols):
                val = row[col]
                text = f"{val:.2f}" if isinstance(val, float) else str(val)
                item = QtWidgets.QTableWidgetItem(text)
                if isinstance(val, (int, float)):
                    item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                item.setFont(QtGui.QFont("Segoe UI", 11))
                table.setItem(r, c, item)

        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        table.resizeColumnsToContents()

        # Expandir "type" para que su contenido se vea completo, mas ancho
        if "type" in cols:
            idx_type = cols.index("type")
            table.setColumnWidth(idx_type, 220)
            table.horizontalHeader().setSectionResizeMode(
                idx_type, QtWidgets.QHeaderView.Fixed
            )
        else:
            table.horizontalHeader().setStretchLastSection(True)

        # Region tambien amplia (nombres largos)
        if "region" in cols:
            idx_region = cols.index("region")
            table.setColumnWidth(idx_region, 180)
            table.horizontalHeader().setSectionResizeMode(
                idx_region, QtWidgets.QHeaderView.Fixed
            )

        for c in range(table.columnCount()):
            if c == (cols.index("type") if "type" in cols else -1):
                continue
            if c == (cols.index("region") if "region" in cols else -1):
                continue
            if table.columnWidth(c) < 90:
                table.setColumnWidth(c, 90)

        layout.addWidget(table)
        return w

    def _build_plot_tab(self):
        w = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(w)
        layout.setContentsMargins(8, 8, 8, 8)

        header = QtWidgets.QLabel("5) Scatter: year vs AveragePrice")
        header.setObjectName("Header")
        sub = QtWidgets.QLabel(f"Regiones: {', '.join(REGIONES)}")
        sub.setObjectName("Subtitle")
        layout.addWidget(header)
        layout.addWidget(sub)

        fig, ax = plt.subplots(figsize=(9, 5))
        fig.patch.set_facecolor("#ffffff")
        colors = ["#1f8a5a", "#2b6cb0", "#d97706"]
        for region, color in zip(REGIONES, colors):
            sub_df = self.df[self.df["region"] == region]
            ax.scatter(
                sub_df["year"],
                sub_df["AveragePrice"],
                label=region,
                alpha=0.65,
                s=22,
                color=color,
                edgecolors="white",
                linewidths=0.4,
            )

        ax.set_xlabel("year", fontsize=11, color="#374151")
        ax.set_ylabel("AveragePrice", fontsize=11, color="#374151")
        ax.set_title("AveragePrice vs year por region", fontsize=13, color="#111827", pad=12)
        ax.legend(frameon=False, loc="upper left")
        ax.grid(True, alpha=0.25, linestyle="--")
        ax.set_facecolor("#f8fafc")
        for spine in ax.spines.values():
            spine.set_color("#e5e9f0")
        fig.tight_layout()

        img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scatter_avocado.png")
        fig.savefig(img_path, dpi=120, facecolor="white")
        print(f"Grafico guardado en: {img_path}")

        canvas = FigureCanvasQTAgg(fig)
        canvas.setStyleSheet("background:#ffffff;")
        layout.addWidget(canvas)
        return w


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setFont(QtGui.QFont("Segoe UI", 10))
    window = AvocadoApp()
    window.show()
    app.exec_()
