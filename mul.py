import time
from numpy.fft import fft, ifft
import numpy as np

def operar(funcion, pila_coeficientes):

    resultado = pila_coeficientes[0]

    # MEDIR TIEMPO
    inicio = time.time()

    for k in range(1,len(pila_coeficientes)):
        resultado = operar_dos_en_dos(funcion, resultado, pila_coeficientes[k])
    
    # MEDIR TIEMPO
    fin = time.time()

    tiempo_trancurrido = fin - inicio

    return resultado, tiempo_trancurrido

def operar_dos_en_dos(funcion, lista_coef_1, lista_coef_2):
    return funcion(lista_coef_1, lista_coef_2)

def mul_con_lagrange():
    pass

def mul_con_vandermonde_r():
    pass


# ---------- Vandermonde en I
def mul_con_vandermonde_i():
    pass

def mul_con_bit_reverso():
    pass

if __name__ == "__main__":
    # pila_coeficientes = 
    
    inicio = time.time()
    for k in range(100):
        a = 100 * 3
    
    fin = time.time()
    xd = fft([1,2,3,4,5,6,7])
    tiempo_transcurrido = (fin-inicio) 
    
    salida_tiempo = f"Tiempo de ejecución: {tiempo_transcurrido * 1e+6:.5f} µs"
    print(salida_tiempo)











def IgualarPolinomios(a, b):
    GradoResultante = len(a) + len(b)  # Grado del polinomio resultante
    TamanoFinal = GradoResultante - 1  # Tamaño deseado de las listas

    # Añadir ceros al final de cada lista para igualar su tamaño al tamaño deseado
    a += [0] * (TamanoFinal - len(a))
    b += [0] * (TamanoFinal - len(b))

    return a, b


def VandermondeI(a,b):
    # Obtener el tamaño de la entrada
    a,b = IgualarPolinomios(a, b)
    N = len(a)

    # Calcular la matriz Vandermonde
    w_n = np.exp(2j * np.pi / N)
    V_n = np.vander(np.array([w_n ** i for i in range(N)]), increasing=True)
    # Evaluacion de coeficientes
    y1 = np.dot(V_n, a)
    y1_redondeado = [round(x.real, 10) + round(x.imag, 10) * 1j for x in y1]
    y2 = np.dot(V_n, b)
    y2_redondeado = [round(x.real, 10) + round(x.imag, 10) * 1j for x in y2]
    # Multiplicación punto (Yk)
    ProductoPunto = [x * y for x, y in zip(y1_redondeado, y2_redondeado)]
    np.set_printoptions(precision=3, suppress=True)

    # Interpolación
    # Inversa de la matriz de vandermonde 
    V_n_inv = np.array([[1/x for x in row] for row in V_n])
    # Vn^-1 . Yk / N
    ResultadoFinal = np.dot(V_n_inv, ProductoPunto)
    ResultadoFinal = ResultadoFinal / len(a)
    ResultadoFinal = np.round(ResultadoFinal).astype(int)
    return ResultadoFinal.tolist()