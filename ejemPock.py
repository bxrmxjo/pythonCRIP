import Pocklington_Lehmer as po
import random
import sys
sys.set_int_max_str_digits(1000000000)

N = 1<<20000 + 1
fact = [2]
print("\n","N = ",N,"\n","Nº dígitos de N: ",len(str(N)),"\n","fact = ",fact,"\n", "¿Es N primo?: ", po.pocklington_lehmer_generalizado(fact,N))

N = (1<<2000) * pow(3,1000) * pow(113,346) + 1
fact = [2,3]
print("\n","N = ",N,"\n","Nº dígitos de N: ",len(str(N)),"\n","fact = ",fact,"\n", "¿Es N primo?: ", po.pocklington_lehmer_generalizado(fact,N))

N = pow(11,593)* pow(23,589) + 1
fact = [11,23]
print("\n","N = ",N,"\n","Nº dígitos de N: ",len(str(N)),"\n","fact = ",fact,"\n", "¿Es N primo?: ", po.pocklington_lehmer_generalizado(fact,N))

N = pow(17,603)* pow(29,104) * (1<<2000) + 1
fact = [2,17,29]
print("\n","N = ",N,"\n","Nº dígitos de N: ",len(str(N)),"\n","fact = ",fact,"\n", "¿Es N primo?: ", po.pocklington_lehmer_generalizado(fact,N))

N = pow(31,603)* pow(6909919,300)*(1<<20000) + 1
fact = [2,31,6909919]
print("\n","N = ",N,"\n","Nº dígitos de N: ",len(str(N)),"\n","fact = ",fact,"\n", "¿Es N primo?: ", po.pocklington_lehmer_generalizado(fact,N))

N = pow(47, 1039)*pow(7,284)*random.randint(1,pow(47,1039))
fact = [7,47]
print("\n","N = ",N,"\n","Nº dígitos de N: ",len(str(N)),"\n","fact = ",fact,"\n", "¿Es N primo?: ", po.pocklington_lehmer_generalizado(fact,N))

#Verificación de primalidad de algunos primos de Proth
ENE = [449,3137,11777,133121,219649,3452929,15998977]
for t in ENE:
    inicio = time.time()
    res = pocklington_lehmer_generalizado([2],t)
    fin = time.time()
    print(f"{t} verifica ser primo: {res}.    TT: {(fin - inicio):.6f}s")
