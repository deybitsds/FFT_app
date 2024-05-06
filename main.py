# Librerias
from PyQt5 import QtWidgets, uic
from polinomios import *

## FUNCIONES

# -- Funciones ventana 1

# ---------- Agregar
def gui_agregar():
    polinomio = mul_window.input_user.text()

    # verificar polinomio correcto
    if not polinomio_es_valido(polinomio):
        mul_window.msj_error.setText("Polinomio ingresado no es válido")
    
    elif len(pila_coeficientes) == 8:
        mul_window.msj_error.setText("Se llenó la memoria :v")

    else:
        # limpiar el mensaje de error
        mul_window.msj_error.setText("")

        # recuperar los coeficientes del polinomio
        lista_coeficientes = recuperar_coeficientes_polinomio_mal_escrito(polinomio)
        
        # corregir la escritura del polinomio
        mensaje = imprimir_polinomio_bien_escrito(lista_coeficientes)
        
        # imprimir la nueva escritura del polinomio en la pila
        pila_polinomios[len(pila_coeficientes)].setText(mensaje)
        
        # agregar la lista de coeficientes a la lista principal        
        pila_coeficientes.append(lista_coeficientes)

# ---------- Multiplicar
def gui_multiplicar():
    pass
    


# ---------- Limpiar
def gui_limpiar():
    global pila_coeficientes
    for t in pila_polinomios:
        t.setText("")
    pila_coeficientes = []

# ---------- Estadisticas
def gui_estadisticas():
    pass

pila_polinomios = []

pila_coeficientes = []

## PROGRAMA PRINCIPAL
if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    # ---------- Archivos UI
    mul_window = uic.loadUi("ventana1.ui")

    pila_polinomios = [mul_window.lbl_pol_0, mul_window.lbl_pol_1,
                        mul_window.lbl_pol_2,mul_window.lbl_pol_3, 
                        mul_window.lbl_pol_4, mul_window.lbl_pol_5, 
                        mul_window.lbl_pol_6, mul_window.lbl_pol_7] 
    
    pila_coeficientes = []

    # ---------- Botones
    
    # Agregar
    mul_window.bt_agregar.clicked.connect(gui_agregar)
    
    # Multiplicar
    mul_window.bt_multiplicar.clicked.connect(gui_multiplicar)

    # Limpiar
    mul_window.bt_limpiar.clicked.connect(gui_limpiar)

    # Estadisticas
    mul_window.bt_estadis.clicked.connect(gui_estadisticas)

    # ---------- Ejecutar
    mul_window.show()
    app.exec()
