"""
Código escrito por Mario Bermejo Cuervo.
email: maberm08@ucm.es
"""

def suma_f27(a, b):
    """Suma dos elementos de F27 representados como listas [a,b,c]"""
    resultado = [0, 0, 0]
    for i in range(3):
        resultado[i] = (a[i] + b[i]) % 3
    return resultado

def negativo_f27(elemento):
    """Devuelve el negativo de un elemento en F27"""
    resultado = [0, 0, 0]
    for i in range(3):
        resultado[i] = (-elemento[i]) % 3
    return resultado

def distancia(w1, w2):
    """
    Calcula la distancia de Hamming entre dos palabras. La distancia entre dos elementos viene dada por:
    distancia([a,b,c],[x,y,z]) = 1 si a=x & b=y & c=z
                               = 0 si a!=x ó b!=y ó c!=z
    """
    dist = 0
    for i in range(5):  # Comparamos las 5 coordenadas
        for j in range(3):  # Comparamos cada componente [a,b,c]
            if w1[i][j] != w2[i][j]:
                dist += 1
                break
    return dist

def generar_elementos_f27():
    """Genera todos los elementos posibles de F27"""
    elementos = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                elementos.append([a, b, c])
    return elementos

def generar_palabras_codigo():
    """
    Genera todas las palabras código a partir de las ecuaciones (manipuladas previamente para ser parametrizadas en función de x1,x5):
    x4 = -x1
    x2 = x1
    x3 = -x1 - x5
    """
    elementos = generar_elementos_f27()
    palabras = []
    
    # Solo necesitamos iterar sobre x1 y x5
    for x1 in elementos:
        for x5 in elementos:
            # Calculamos las demás coordenadas usando las ecuaciones parametrizadas previamente.
            x2 = x1.copy() 
            x4 = negativo_f27(x1)  
            x3 = negativo_f27(suma_f27(x1, x5))
            
            palabra = [x1, x2, x3, x4, x5]
            palabras.append(palabra)
    return palabras

def palabra_mas_cercana(w):
    """
    Encuentra la palabra código más cercana a w. No es seguro que dicha palabra sea única,
    por lo que devolerá una de las palabras cuya distancia a w sea la mínima posible.
    """
    palabras_codigo = generar_palabras_codigo()
    distancia_min = 5 #Inicializamos la distancia en el máximo valor que pueda tomar.
    palabra_cercana = None 
    
    for palabra in palabras_codigo:
        dist = distancia(w, palabra)
        if dist < distancia_min:
            distancia_min = dist
            palabra_cercana = palabra

    return palabra_cercana
