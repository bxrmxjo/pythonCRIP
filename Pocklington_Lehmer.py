import math

def gcd_binario_tail_rec_fancy(x, y):  # (x,y) != (0,0)
    x = abs(x)
    y = abs(y)
    s = 0
    while x != 0 and y != 0:
        xespar = x & 1 == 0
        yespar = y & 1 == 0
        if xespar and yespar:
            s += 1                # m = 2**s = 1 << s
            x >>= 1
            y >>= 1
        elif xespar:
            x >>= 1
        elif yespar:
            y >>= 1
        elif x > y:
            x = (x - y) >> 1
        else:
            y = (y - x) >> 1
    if x == 0:                    # caso base: gcd(0,y)=y
        m = y << s
    else:                         # caso base: gcd(x,0)=x
        m = x << s
    return m

def pocklington_lehmer_generalizado(n):
    if n < 2:
        return False  # Números menores que 2 no son primos
    if n in (2, 3):
        return True  # 2 y 3 son primos
    
    # Factorizar n - 1
    n_menos_1 = n - 1
    A = 1
    factores_primos_A = []   
    copia_n_menos_1 = n_menos_1
    """
    A continuación, se obtienen factores primos (en orden) de n-1, y se guardan en factores_primos_A.
    Se extraen todas las potencias de dichos primos del propio n-1, de forma que A no comparte divisores
    con (n-1)/A = B
    
    """

    #Obtenemos los factores primos de A, así como el propio A (que debe se mayor que raíz de n)
    if copia_n_menos_1 % 2 == 0:
            factores_primos_A.append(2)
            
            while copia_n_menos_1 % 2 == 0:
                A *= 2
                copia_n_menos_1 //= 2 #Eliminamos el factor primo de n-1
    i = 3    
    while A < math.sqrt(n_menos_1):
        if copia_n_menos_1 % i == 0:
            factores_primos_A.append(i)
            

            while copia_n_menos_1 % i == 0:
                A *= i
                copia_n_menos_1 //= i #Eliminamos el factor primo de n-1
        i += 2


    # Probar varios valores de a
    is_prime = True

    for f in factores_primos_A: #Tratamos de buscar nuestro a_p

        # Comprobamos las condiciones de Pocklington-Lehmer
        for a in range(2, n-2):
            # Calculamos a^((n-1)/d) mod n usando pow()
            if pow(a, n_menos_1 // f, n) == 1:
                if gcd_binario_tail_rec_fancy(pow(a,(n-1)//f),n) == 1:
                    is_prime = True 
                    print(a," Se ha encontrado")
                    break              
            else: 
                return False #n no es primo como consecuencia del pequeño teorema de Fermat
        


    return is_prime

        
def exp_binaria_mod(base, exp, mod):
    result = 1
    base = base % mod  # Aseguramos que la base esté dentro del rango del módulo
    while exp > 0:
        if exp % 2 == 1:  # Si el exponente es impar
            result = (result * base) % mod  # Multiplica y aplica el módulo
        base = (base * base) % mod  # Cuadra la base y aplica el módulo
        exp //= 2  # Reduce el exponente a la mitad
    return result
