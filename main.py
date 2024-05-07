# Librerias
from PyQt5 import QtWidgets, uic
from polinomios import *
from mul import *

## FUNCIONES

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

        # limpiar la caja de input
        mul_window.input_user.setText("")

# ---------- Multiplicar
def gui_multiplicar():
    
    opcion_actual = mul_window.comboBox.currentText()
    
    resultado, tiempo_trancurrido = operar(diccionario_funciones[opcion_actual], pila_coeficientes)
    
    salida_resultado = imprimir_polinomio_bien_escrito(resultado)
    mul_window.msj_resul.setText(resultado)

    salida_tiempo = f"Tiempo de ejecución: {tiempo_transcurrido * 1e+6:.5f} µs"
    mul_window.msj_tiempo.setText(salida_tiempo)

 # ---------- Limpiar
def gui_limpiar():
    global pila_coeficientes
    
    for t in pila_polinomios:
        t.setText("")
    
    mul_window.msj_resul.setText("")
    mul_window.msj_tiempo.setText("")
    mul_window.input_user.setText("")
    mul_window.msj_error.setText("")

    pila_coeficientes = []
    

# ---------- Estadisticas
def gui_estadisticas():
    est_window.show()

def gui_volver():
    est_window.hide()

pila_polinomios = []

pila_coeficientes = []

diccionario_funciones = {"Lagrange": mul_con_lagrange,
                        "Vandermonde en R":mul_con_vandermonde_r,
                        "Vandermonde en I":mul_con_vandermonde_i,
                        "Bit reverso": mul_con_bit_reverso}

## PROGRAMA PRINCIPAL
if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    # ---------- Archivos UI
    mul_window = uic.loadUi("mul_fft.ui")
    est_window = uic.loadUi("estadisticas.ui")

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

    # Volver a principal
    est_window.bt_volver.clicked.connect(gui_volver)

    # ---------- Ejecutar
    mul_window.show()
    app.exec()
