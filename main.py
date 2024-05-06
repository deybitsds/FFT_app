from PyQt5 import QtWidgets, uic
from ventana1 import *
from ventana2 import *

## FUNCIONES

# -- Funciones ventana 1

# -- Funciones ventana 2

## PROGRAMA PRINCIPAL
app = QtWidgets.QApplication([])

# cargar archivos .ui
program = uic.loadUi("ventana1.ui")
resultado = uic.loadUi("ventana2.ui")

# Botones
program.boton_calcular.clicked.connect(gui_program)

# Ejecutar
program.show()
app.exec()

def algoritmo(lista_valores):
    # El algoritmo

    return lista_coeficientes
S

def main():
    # leer coeficientes usuario
    lista_coeficientes = [1,2,0,4] # 1 + 2x + 0x² + 4x³
    # siempre len(lista_coef) será multiplo de 2

    lista_puntos1 = funcion_de_evaluar(lista_coeficientes)
    lista_puntos2 = funcion_de_evaluar(lista_coeficientes)

    # multiplicamos los puntos
    lista_puntos_multiplicacion = multiplicar(lista_puntos1, lista_puntos2)

    lista_coeficientes_resultado = funcion_interpolar(lista_puntos_multiplicacion)

