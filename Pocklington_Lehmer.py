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
 
#Ejemplos

# N = 4636016641
# fact = [2]
# print("\n","N = ",N,"\n","fact = ",fact,"\n", "¿Es N primo?: ", pocklington_lehmer_generalizado(fact,N))

N = 1<<20000 + 1
fact = [2]
print("\n","N = ",N,"\n","Nº dígitos de N: ",len(str(N)),"\n","fact = ",fact,"\n", "¿Es N primo?: ", pocklington_lehmer_generalizado(fact,N))

N = (1<<2000) * pow(3,1000) * pow(113,346) + 1
fact = [2,3]
print("\n","N = ",N,"\n","Nº dígitos de N: ",len(str(N)),"\n","fact = ",fact,"\n", "¿Es N primo?: ", pocklington_lehmer_generalizado(fact,N))

N = pow(11,593)* pow(23,589) + 1
fact = [11,23]
print("\n","N = ",N,"\n","Nº dígitos de N: ",len(str(N)),"\n","fact = ",fact,"\n", "¿Es N primo?: ", pocklington_lehmer_generalizado(fact,N))

N = pow(17,603)* pow(29,104) * (1<<2000) + 1
fact = [2,17,29]
print("\n","N = ",N,"\n","Nº dígitos de N: ",len(str(N)),"\n","fact = ",fact,"\n", "¿Es N primo?: ", pocklington_lehmer_generalizado(fact,N))

N = pow(31,603)* pow(6909919,300)*(1<<20000) + 1
fact = [2,31,6909919]
print("\n","N = ",N,"\n","Nº dígitos de N: ",len(str(N)),"\n","fact = ",fact,"\n", "¿Es N primo?: ", pocklington_lehmer_generalizado(fact,N))


#Primos proth
ENE = [449,3137,11777,133121,219649]
for t in ENE:
    inicio = time.time()
    res = pocklington_lehmer_generalizado([2],t)
    fin = time.time()
    print(f"{t} verifica ser primo: {res}.    TT: {(fin - inicio):.6f}")



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
            if pocklington_lehmer_generalizado([2], numero_proth) and numero_proth not in primos_proth:
                primos_proth.add(numero_proth)
    fin = time.time()
    print(sorted(primos_proth))
    print(f"cantidad primos de Proth con n entre {cota_inf} y {cota_sup} : {len(primos_proth)}.   TT: {(fin-inicio):.6f} s")

print("\n")
encontrar_primos_proth(10)



# encontrar_primos_proth(12)
# [3, 5, 13, 17, 41, 97, 113, 193, 241, 257, 353, 449, 577, 641, 673, 769, 929, 1153, 1217, 1409, 1601, 2113, 2689, 2753, 3137, 3329, 3457, 4481, 4993, 6529, 7297, 7681, 7937, 9473, 9601, 9857, 10369, 10753, 11393, 11777, 12161, 12289, 13313, 13441, 13697, 14081, 14593, 15233, 15361, 16001, 17921, 18433, 19457, 22273, 23041, 23297, 25601, 26113, 26881, 30977, 31489, 32257, 36097, 36353, 37633, 37889, 39937, 40193, 41729, 43777, 45569, 46337, 49409, 49921, 50177, 51713, 57089, 57601, 58369, 59393, 60161, 61441, 64513, 67073, 70657, 76289, 76801, 79873, 80897, 81409, 83969, 84481, 86017, 87041, 87553, 95233, 96769, 101377, 102913, 112129, 113153, 115201, 118273, 119297, 119809, 120833, 125441, 133121, 133633, 136193, 138241, 143873, 151553, 153089, 155137, 158209, 159233, 161281, 168449, 170497, 176129, 176641, 183809, 184321, 187393, 202753, 211457, 211969, 216577, 219649, 220673, 226817, 228353, 232961, 235009, 238081, 240641, 242689, 249857, 251393, 254977, 260609, 279553, 285697, 295937, 301057, 307201, 310273, 320513, 326657, 329729, 331777, 345089, 357377, 365569, 366593, 380929, 384001, 394241, 414721, 424961, 428033, 430081, 455681, 463873, 464897, 471041, 473089, 495617, 498689, 514049, 520193, 525313, 531457, 534529, 566273, 572417, 575489, 577537, 592897, 617473, 623617, 642049, 643073, 649217, 658433, 667649, 673793, 675841, 685057, 694273, 695297, 703489, 706561, 715777, 721921, 724993, 746497, 747521, 765953, 771073, 772097, 783361, 790529, 793601, 795649, 796673, 808961, 812033, 814081, 817153, 833537, 836609, 838657, 854017, 858113, 875521, 878593, 879617, 890881, 904193, 918529, 921601, 928769, 930817, 946177, 959489, 962561, 964609, 979969, 986113, 995329, 1017857, 1022977, 1038337, 1054721, 1062913, 1067009, 1075201, 1079297, 1093633, 1103873, 1124353, 1161217, 1191937, 1198081, 1210369, 1239041, 1251329, 1288193, 1312769, 1320961, 1345537, 1355777, 1370113, 1374209, 1423361, 1437697, 1454081, 1492993, 1503233, 1509377, 1517569, 1533953, 1546241, 1579009, 1595393, 1607681, 1628161, 1652737, 1669121, 1689601, 1708033, 1714177, 1724417, 1732609, 1748993, 1751041, 1841153, 1847297, 1865729, 1923073, 1964033, 2021377, 2052097, 2101249, 2107393, 2119681, 2123777, 2148353, 2209793, 2254849, 2297857, 2314241, 2357249, 2363393, 2369537, 2377729, 2387969, 2414593, 2437121, 2455553, 2469889, 2486273, 2492417, 2512897, 2516993, 2543617, 2553857, 2574337, 2592769, 2598913, 2639873, 2641921, 2652161, 2660353, 2664449, 2707457, 2715649, 2721793, 2756609, 2775041, 2787329, 2795521, 2836481, 2856961, 2869249, 2910209, 2912257, 2922497, 2930689, 2936833, 2942977, 2979841, 3002369, 3008513, 3053569, 3076097, 3082241, 3115009, 3127297, 3133441, 3168257, 3174401, 3198977, 3237889, 3266561, 3274753, 3280897, 3291137, 3305473, 3348481, 3360769, 3373057, 3414017, 3420161, 3428353, 3438593, 3452929, 3469313, 3500033, 3526657, 3543041, 3557377, 3573761, 3581953, 3598337, 3606529, 3635201, 3647489, 3655681, 3684353, 3690497, 3721217, 3782657, 3819521, 3844097, 3870721, 3893249, 3911681, 3919873, 3926017, 3942401, 3944449, 3960833, 3985409, 3993601, 4003841, 4012033, 4085761, 4141057, 4151297, 4165633, 4171777, 4188161, 4206593, 4263937, 4304897, 4427777, 4435969, 4452353, 4476929, 4550657, 4632577, 4771841, 4780033, 4845569, 4902913, 5050369, 5066753, 5140481, 5189633, 5222401, 5246977, 5287937, 5337089, 5345281, 5369857, 5410817, 5492737, 5517313, 5591041, 5632001, 5656577, 5738497, 5763073, 5779457, 5804033, 5910529, 5951489, 5984257, 6000641, 6008833, 6082561, 6156289, 6230017, 6254593, 6320129, 6393857, 6402049, 6574081, 6737921, 6885377, 6942721, 7057409, 7065601, 7090177, 7114753, 7139329, 7188481, 7229441, 7352321, 7360513, 7434241, 7475201, 7548929, 7630849, 7671809, 7704577, 7729153, 7745537, 7925761, 8040449, 8114177, 8122369, 8163329, 8245249, 8286209, 8318977, 8441857, 8466433, 8753153, 8851457, 8876033, 8949761, 9023489, 9031681, 9080833, 9220097, 9326593, 9392129, 9441281, 9547777, 9588737, 9646081, 9695233, 9711617, 9760769, 9834497, 10039297, 10063873, 10162177, 10186753, 10334209, 10383361, 10457089, 10473473, 10498049, 10571777, 10579969, 10629121, 10678273, 10702849, 10842113, 10924033, 10940417, 10989569, 10997761, 11038721, 11046913, 11087873, 11112449, 11169793, 11186177, 11309057, 11358209, 11456513, 11653121, 11677697, 11759617, 11898881, 11907073, 12021761, 12046337, 12070913, 12128257, 12177409, 12193793, 12226561, 12390401, 12521473, 12587009, 12644353, 12685313, 12759041, 12767233, 12808193, 12865537, 12906497, 12931073, 13004801, 13029377, 13037569, 13135873, 13152257, 13283329, 13332481, 13381633, 13496321, 13570049, 13578241, 13766657, 14012417, 14036993, 14110721, 14118913, 14241793, 14258177, 14282753, 14307329, 14340097, 14430209, 14438401, 14610433, 14651393, 14684161, 14749697, 14774273, 14831617, 14872577, 14880769, 14970881, 15052801, 15167489, 15200257, 15298561, 15372289, 15470593, 15511553, 15618049, 15732737, 15781889, 15790081, 15831041, 15962113, 15978497, 16125953, 16355329, 16371713, 16494593, 16519169, 16592897, 16617473, 16650241, 16674817, 16699393]
# cantidad primos de Proth con n entre 1 y 12 : 596.   TT: 2027.354085 s


