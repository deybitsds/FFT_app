def recuperar_coeficientes_polinomio_mal_escrito(string):
    pass

def imprimir_polinomio_bien_escrito(lista_coeficientes):
    grado = len(lista_coeficientes) - 1
    polinomio = ""

    for i, coeficiente in reversed(list(enumerate(lista_coeficientes))):
        if coeficiente != 0:
            if i == 0:
                polinomio += f"{coeficiente}"
            elif i == 1:
                polinomio += f"{coeficiente}x"
            else:
                polinomio += f"{coeficiente}x^{i}"

            if i != 0:
                polinomio += " + "
    return polinomio

def polinomio_es_valido(string):
    return #True

if __name__ == "__main__":
    print("xd")
