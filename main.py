## LIBRERIAS

# -- Librerias para el grafico
import matplotlib
matplotlib.use('Qt5Agg')  # Especificar el backend Qt5Agg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# -- Librerias para el manejo de la UI
from PyQt5 import QtWidgets, uic

# -- importar loas guis
import main2_ui
import estadisticas_ui

# -- Llamada a modulos de polinomios
from polinomios import *
from mul import *

## FUNCIONES

# ---------- Agregar
def gui_agregar():
    polinomio = mul_window.input_user.text()

    # verificar polinomio correcto
    if polinomio.replace(" ", "") == "" or not polinomio_es_valido(polinomio):
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

# ---------- Eliminar
def gui_eliminar():
    global pila_coeficientes

    mul_window.input_user.setText("")
    
    pila_polinomios[len(pila_coeficientes) - 1].setText("")

    pila_coeficientes.pop()

# ---------- Multiplicar
def gui_multiplicar():
    
    if not pila_coeficientes:
        mul_window.msj_error.setText("No hay polinomios ingresados")
        return 

    opcion_actual = mul_window.comboBox.currentText()
    resultado = operar(opcion_actual = opcion_actual, lista_coeficientes = pila_coeficientes)
    
    salida_resultado = imprimir_polinomio_bien_escrito(resultado)
    mul_window.msj_resul.setText(salida_resultado)
     
    tiempo_transcurrido = diccionario_tiempos[opcion_actual]

    establecer_tiempos(opcion_actual, pila_coeficientes)

    salida_tiempo = f"Tiempo de ejecución: {tiempo_transcurrido:.5f} µs"
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
    # Crear una instancia de la ventana principal
    
    # Obtener una referencia al QVBoxLayout
    layout = ui_est.qv_imagen
    
    limpiar_grafico(layout)
    actualizar_grafico(layout)

    waza1.show()
    waza.hide()
    est_window.bt_volver.clicked.connect(gui_volver)

    
def gui_volver():
    waza.show()
    waza1.hide()

def actualizar_grafico(layout):
    
    # Datos para la gráfica
    nombres = ['Lagrange', 'Vandermonde \nen R', 'Vandermonde \nen I', 'Bit Reverso']
    tiempos = recuperar_tiempos()

    # Definir una paleta de colores
    colores = ['red', 'green', 'blue', 'purple']

    # Crear la figura y el lienzo de Matplotlib
    fig, ax = plt.subplots()
    ax.bar(nombres, tiempos, color=colores)

    # ax.plot(nombres, tiempos)
    ax.set_xlabel('Método')
    ax.set_ylabel('Tiempo de ejecución (µ segundos)')
    ax.set_title('Comparación de Tiempos de Ejecución')
    ax.grid(True)


    # Crear el lienzo de la gráfica de Matplotlib como un widget de PyQt5
    canvas = FigureCanvas(fig)
    
    # Obtener el QVBoxLayout de la ventana principal
    # layout = est_window.findChild(QtWidgets.QVBoxLayout, 'qv_imagen')
    
    # Agregar el widget de la gráfica al QVBoxLayout
    layout.addWidget(canvas)

def limpiar_grafico(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()

def recuperar_tiempos():
    return [valor for valor in diccionario_tiempos.values()]

# ---------- Operar
def operar(opcion_actual, lista_coeficientes):
    global diccionario_tiempos, diccionario_funciones

    funcion = diccionario_funciones[opcion_actual]

    resultado = lista_coeficientes[0]

    # MEDIR TIEMPO
    inicio = time.time()

    for k in range(1,len(lista_coeficientes)):
        resultado = operar_dos_en_dos(funcion, resultado, lista_coeficientes[k])
    
    # MEDIR TIEMPO
    fin = time.time()

    tiempo_transcurrido = fin - inicio

    # establecer todos los valores del diccionario con el tiempo transcurrido del algoritmo actual
    diccionario_tiempos[opcion_actual] = tiempo_transcurrido * 1e6

    return resultado

def establecer_tiempos(opcion_actual, lista_coeficientes):
    global diccionario_tiempos

    for clave in diccionario_tiempos:
        if clave != opcion_actual:
            operar(opcion_actual = clave, lista_coeficientes = lista_coeficientes)

# -- 
## PROGRAMA PRINCIPAL
pila_polinomios = []

pila_coeficientes = []

diccionario_funciones = {"Lagrange": mul_con_lagrange,
                        "Vandermonde en R":mul_con_vandermonde_r,
                        "Vandermonde en I":mul_con_vandermonde_i,
                        "Bit reverso": mul_con_bit_reverso}

diccionario_tiempos = {"Lagrange": 0.0,
                        "Vandermonde en R": 0.0,
                        "Vandermonde en I": 0.0,
                        "Bit reverso": 0.0}

if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    # Crear instancias de QMainWindow
    mul_window = QtWidgets.QMainWindow()
    est_window = QtWidgets.QMainWindow()

    waza = mul_window
    waza1 = est_window

    # Cargar archivos .ui convertidos
    mul_window = main2_ui.Ui_window()
    mul_window.setupUi(waza)
    ui_mul = mul_window

    est_window = estadisticas_ui.Ui_window()
    est_window.setupUi(waza1)
    ui_est = est_window

    pila_polinomios = [ui_mul.lbl_pol_0, ui_mul.lbl_pol_1,
                        ui_mul.lbl_pol_2, ui_mul.lbl_pol_3, 
                        ui_mul.lbl_pol_4, ui_mul.lbl_pol_5, 
                        ui_mul.lbl_pol_6, ui_mul.lbl_pol_7] 
        
    pila_coeficientes = []

    # Conectar señales a slots
    ui_mul.bt_agregar.clicked.connect(gui_agregar)
    ui_mul.bt_multiplicar.clicked.connect(gui_multiplicar)
    ui_mul.bt_eliminar.clicked.connect(gui_eliminar)
    ui_mul.bt_limpiar.clicked.connect(gui_limpiar)
    ui_mul.bt_estadis.clicked.connect(gui_estadisticas)
    ui_est.bt_volver.clicked.connect(gui_volver)

    # Mostrar las ventanas
    waza.show()
    app.exec_()