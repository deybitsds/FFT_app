# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# import sys

# class MiVentana(QMainWindow):
#     def __init__(self, parent=None):
#         QMainWindow.__init__(self, parent)
        
#         # Cargar el archivo .ui
#         uic.loadUi('estadisticas.ui', self)

#         # Crear el objeto Figure
#         fig = Figure()

#         # Crear el lienzo que permitirá mostrar Figure en la GUI
#         canvas = FigureCanvas(fig)

#         # Añadir el lienzo al layout
#         self.verticalLayout.addWidget(canvas)

#         # Generar el gráfico dentro de Figure
#         ax = fig.add_subplot(111)
#         ax.plot([1, 2, 3, 4, 5])

# def mostrar_grafico():
#     app = QApplication(sys.argv)

#     ventana = MiVentana()
#     ventana.show()

#     sys.exit(app.exec_())

# def gui_estadisticas():
#     mostrar_grafico()

# mostrar_grafico()