import time
from numpy.fft import fft, ifft
import numpy as np

# ---------- Operar
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

# ---------- Lagrange
def mul_con_lagrange(lista_1, lista_2):
    return mul_con_vandermonde_r(lista_1, lista_2)

# ---------- Vandermonde en R
def mul_con_vandermonde_r(coef_poli1, coef_poli2):
    coef_poli1, coef_poli2 = IgualarPolinomios(coef_poli1, coef_poli2)
    # Generar matrices de vandermonde en R
    matriz_poli1 = matriz_vandermonde(generar_valores(len(coef_poli1)))
    matriz_poli2 = matriz_vandermonde(generar_valores(len(coef_poli2)))

    ev_pol1 = np.dot(matriz_poli1, coef_poli1)
    ev_pol2 = np.dot(matriz_poli2, coef_poli2)

    # Multiplicacion punto
    producto_punto = ev_pol1 * ev_pol2

    # Interpolación
    inversa_vandermonde = np.linalg.inv(matriz_poli1)
    resultado = np.dot(inversa_vandermonde, producto_punto)
    ResultadoFinal = np.round(resultado).astype(int)
    return ResultadoFinal.tolist()

def completar_con_ceros(lista):
    longitud_actual = len(lista)
    siguiente_potencia_dos = 1
    while siguiente_potencia_dos < longitud_actual:
        siguiente_potencia_dos *= 2
    
    # Si la longitud actual ya es una potencia de 2, no hay necesidad de completar con ceros
    if longitud_actual == siguiente_potencia_dos:
        return lista  
    # Calcular cuántos ceros se deben agregar
    ceros_a_agregar = siguiente_potencia_dos - longitud_actual
    lista_completa = lista + [0] * ceros_a_agregar
    return lista_completa

def matriz_vandermonde(valores):
    n = len(valores)
    matriz = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            matriz[i][j] = valores[i]**j

    return matriz

def generar_valores(n):
    l = []
    for k in range(n):
        l.append(k)
    return l

# ---------- Vandermonde en I
def mul_con_vandermonde_i(a,b):
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

def IgualarPolinomios(a, b):
    GradoResultante = len(a) + len(b)  # Grado del polinomio resultante
    TamanoFinal = GradoResultante - 1  # Tamaño deseado de las listas

    # Añadir ceros al final de cada lista para igualar su tamaño al tamaño deseado
    a += [0] * (TamanoFinal - len(a))
    b += [0] * (TamanoFinal - len(b))

    return a, b

# ---------- Bit reverso
def mul_con_bit_reverso(A, B):
    m = len(A)
    n = len(B)
    k = m + n - 1

    # Asegúrate de que k sea una potencia de 2
    k = 2 ** (int(np.log2(k)) + 1)

    A.extend([0] * (k - m))
    B.extend([0] * (k - n))

    ya = FFT(A)
    yb = FFT(B)

    yc = [ya[i] * yb[i] for i in range(k)]

    C = [round(val.real) for val in IFFT(yc)]

    return C[:m+n-1]


def bit_reverso(n):
    num_bits = int(np.log2(n))
    indices_reversos = [0] * n
    for i in range(n):
        indices_reversos[i] = int(
            format(i, '0' + str(num_bits) + 'b')[::-1], 2)
    return indices_reversos


def FFT(P):
    n = len(P)
    indices = bit_reverso(n)
    P = [P[i] for i in indices]

    for s in range(1, int(np.log2(n)) + 1):
        m = 2 ** s
        w_m = np.exp(-2 * np.pi * 1j / m)
        for k in range(0, n, m):
            w = 1
            for j in range(m // 2):
                t = w * P[k + j + m // 2]
                u = P[k + j]
                P[k + j] = u + t
                P[k + j + m // 2] = u - t
                w = w * w_m

    return P


def IFFT(P):
    n = len(P)
    indices = bit_reverso(n)
    P = [P[i] for i in indices]

    for s in range(1, int(np.log2(n)) + 1):
        m = 2 ** s
        w_m = np.exp(2 * np.pi * 1j / m)
        for k in range(0, n, m):
            w = 1
            for j in range(m // 2):
                t = w * P[k + j + m // 2]
                u = P[k + j]
                P[k + j] = u + t
                P[k + j + m // 2] = u - t
                w = w * w_m

    P = [val / n for val in P]

    return P

# ---------- Principal
if __name__ == "__main__":
    # pila_coeficientes = 
    
    A = [-1,2,0,0,3]
    B = [-6,5,0,4]

    print(mul_con_bit_reverso(A,B))