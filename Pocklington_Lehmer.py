import math
import sys
import time
sys.set_int_max_str_digits(1000000000)


def pocklington_lehmer_generalizado(factores_primos_A:list, n:int):
    """
    Dado n del que se quiere conocer su primalidad, se introduce como argumento la lista
    de factores primos de A, donde n-1 = A*B y A no comparte factores primos con B (pues
    han de ser coprimos). No se necesita que se introduzca A, ya que se calculará dentro
    del programa al ser fácil y rápido (habitualmente). Es necesario que A sea mayor que sqrt(n)
    """
    n_menos_1 = n - 1
    copia_n_menos_1 = n - 1
    A = 1

    #Calculamos A a partir de sus factores primos.
    #SI SE SABE QUE A > sqrt(n-1) NO HACE FALTA ESTE BUCLE NI EL IF
    # for t in factores_primos_A:
    #     while copia_n_menos_1%t == 0:
    #         A *= t
    #         copia_n_menos_1 //= t

    # if A**2 < n_menos_1:
    #     raise ValueError("La factorización de A no es lo suficientemente grande")

    #pequeño truquito porque n - 1 = 2
    if n_menos_1 == 2:
        return True

    for f in factores_primos_A: #Tratamos de buscar nuestro a_p

        is_prime = False
        # Comprobamos las condiciones de Pocklington-Lehmer
        for a in range(2, n-2):
            # Calculamos a^((n-1)/d) mod n usando pow()
            

            #math.gcd() es más eficiente que gcd_ext_binario_fancy porque está implementado internamente
            #en C en vez de sobrecarga el interprete de python.
            if pow(a, n_menos_1, n) == 1:
                if math.gcd(pow(a,(n-1)//f)-1,n) == 1: 
                    is_prime = True 
                    break              
            else:
                return False #n no es primo como consecuencia del pequeño teorema de Fermat
        if is_prime == False:
            return False
        

    return is_prime
 
