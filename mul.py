import time
import numpy as np

# ---------- Operar
def operar_dos_en_dos(funcion, lista_coef_1, lista_coef_2):
    return funcion(lista_coef_1, lista_coef_2)

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

# ---------- Lagrange
def mul_con_lagrange(A, B):
    # Igualar longitudes de los polinomios
    if len(A) < len(B):
        A += [0] * (len(B) - len(A)) 
    if len(A) > len(B):
        B += [0] * (len(A) - len(B)) 
    # Evaluación usando Horner
    evaluacion_A = evaluacion_horner(A)  # Evaluar el polinomio A
    evaluacion_B = evaluacion_horner(B)  # Evaluar el polinomio B
    return operar_lagrange(A, B)
    # Multiplicación punto a punto de las evaluaciones
    multiplicacion_punto_a_punto = [evaluacion_A[x] * evaluacion_B[x] for x in range(len(A) + 1)]
    
    # Interpolación para obtener los coeficientes del polinomio resultante
    coeficientes = interpolacion_lagrange([i for i in range(len(A) + 1)], multiplicacion_punto_a_punto)
    # Retornar coeficientes
    return coeficientes

# Módulo Evaluación con horner
def evaluacion_horner(A):
    n = len(A) + 1  # Tamaño del polinomio evaluado
    x = [i for i in range(n)]  # Lista de puntos de evaluación
    resultado = [A[-1] for _ in range(n)]  # Resultado inicial basado en el último coeficiente

    # Evaluación usando el método de Horner
    for k in range(n):
        for i in reversed(range(1, len(A))):  # Recorre los coeficientes de derecha a izquierda
            resultado[k] = x[k] * resultado[k] + A[i-1]  # Aplicación del método de Horner
    # Retornar resultado
    return resultado
def operar_lagrange(A, B):
    return mul_con_vandermonde_i(A,B)
# Módulo Convolución
def convolucion(A, B):
    # Inicializar una lista para almacenar los coeficientes del resultado de la convolución
    coeficientes = [0 for _ in range(len(A) + len(B) - 1)]

    # Realizar la convolución (multiplicación de polinomios)
    for i in range(len(A)):
        for j in range(len(B)):
            coeficientes[i + j] += A[i] * B[j]  # Actualiza el coeficiente correspondiente
    # Retornar coeficientes
    return coeficientes

# Módulo de Interpolación de Lagrange
def interpolacion_lagrange(x, y):
    coeficientes = []
    polinomios_parciales = []
    n = len(x)  # Número de puntos
    
    # Construir polinomios parciales para la interpolación
    for i in range(n):
        denominador, numerador = 1, [1, 0]  # Inicializar el numerador y el denominador
        for j in range(n):
            if i != j:
                denominador *= x[i] - x[j]  # Calcular el denominador
                numerador = convolucion(numerador, [-x[j], 1])  # Calcular el numerador parcial
        
        # Ajustar el numerador por el valor correspondiente de y y el denominador
        numerador = [k / denominador * y[i] for k in numerador]
        polinomios_parciales.append(numerador)
    
    # Sumar los polinomios parciales para obtener el polinomio interpolado
    for i in range(n):
        coeficientes.append(sum([polinomios_parciales[j][i] for j in range(n)]))
    #Retornar coeficientes
    return coeficientes

    
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