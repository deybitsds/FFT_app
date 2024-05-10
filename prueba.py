from PyQt5 import QtWidgets
import estadisticas_ui
import main2_ui

app = QtWidgets.QApplication([])

estadisticas_window = QtWidgets.QMainWindow()  # Cambia QWidget a QMainWindow
ui_estadisticas = estadisticas_ui.Ui_window()
ui_estadisticas.setupUi(estadisticas_window)

main_window = QtWidgets.QMainWindow()  # Cambia QWidget a QMainWindow
ui_main = main2_ui.Ui_window()
ui_main.setupUi(main_window)

# Utiliza tus ventanas como necesites
estadisticas_window.show()
main_window.show()

app.exec_()
