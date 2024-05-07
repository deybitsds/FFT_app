import re

# ---------- Coeficientes
def recuperar_coeficientes_polinomio_mal_escrito(string):
    cadena = borrar_espacios(string)
    if "^-" in cadena or re.search(r'[^0-9+\-*x^ ]', cadena):
        return None
    else:
        return coefs(cadena)

def coefs(entrada):
  regexp = r"(-?\d*)(x?)(?:(?:\^|\\)(\d))?"
  c = {}
  for coef, x, exp in re.findall(regexp, entrada):
    # print(coef, x, exp)
    if not coef and not x:
      continue
    if x and not coef:
      coef = '1'
    if x and coef == "-":
      coef = "-1"
    if x and not exp:
      exp = '1'
    if coef and not x:
      exp = '0'
    exp = ord(exp) & 0x000F
    if exp in c:
        c[exp] += float(coef)
    else:
        c[exp] = float(coef)
  grado = max(c)
  coeficientes = [0.0] * (grado+1)
  for g, v in c.items():
    coeficientes[g] = v
  return [int(numero) for numero in coeficientes]
  
def borrar_espacios(a):
    a = a.replace(" ", "")
    return a

# ---------- Imprimir nuevo polinomio
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
    return recuperar_coeficientes_polinomio_mal_escrito(string)

if __name__ == "__main__":
    print(recuperar_coeficientes_polinomio_mal_escrito("1 + 2x"))
