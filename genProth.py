import math,sys,time
import Pocklington_lehmer as po


#https://oeis.org/A080076/b080076.txt lista de primos de proth ordenados.
def encontrar_primos_proth(cota_sup, cota_inf=1):
    """
    Busca primos de Proth de la forma k*2^n + 1, donde k es impar y 2^n > k.
    Los números generados están en el rango de exponentes [cota_inf, cota_sup].
    Como k solo toma valores impares, es posible que para un "n" determinado se
    genere un primo de proth mayor que otro primo de proth asociado a un "n0" mayor a "n"
    """
    inicio = time.time()
    primos_proth = set()
    for n in range(cota_inf, cota_sup + 1):
        doselevadoan = 1 << n
        # k debe ser impar y menor que 2^n. 
        for k in range(1, doselevadoan, 2):  # k es impar, por lo que incrementamos de 2 en 2
            numero_proth = k * doselevadoan + 1

                # Usamos pocklington_lehmer_generalizado para comprobar si es primo
            if po.pocklington_lehmer_generalizado([2], numero_proth) and numero_proth not in primos_proth:
                primos_proth.add(numero_proth)
    fin = time.time()
    print(sorted(primos_proth))
    print(f"cantidad primos de Proth con n entre {cota_inf} y {cota_sup} : {len(primos_proth)}.   TT: {(fin-inicio):.6f} s")

print("\n")
encontrar_primos_proth(10)
