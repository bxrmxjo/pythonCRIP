# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:36:24 2024

@author:Alberto Herencia Arce
con Miguel Uribe, Pablo Esteve y Mario Bermejo

"""
def raiz_cuadrada_techo(n): 
    #Modificamos la función de raiz cuadrada para truncar hacia arriba las raices
    #no enteras
    izq = 0             
    der = n + 1
    while izq < der - 1:
        med = (izq + der) // 2
        if med * med <= n:
            izq = med
        else:
            der = med
    # Comprobamos si hay que truncar hacia arriba
    if izq * izq < n:
        return izq + 1
    else:
        return izq

def gcd_extendido_binario(x,y):             # (x,y) != (0,0)
    xespar = x%2 == 0
    yespar = y%2 == 0
    if x < 0:
        m,a,b = gcd_extendido_binario(-x,y)
        a = -a
    elif y < 0:
        m,a,b = gcd_extendido_binario(x,-y)
        b = -b
    elif x == 0:                  # caso base: gcd(0,y)=y
        m,a,b = y,0,1
    elif y == 0:                  # caso base: gcd(x,0)=x
        m,a,b = x,1,0
    elif xespar and yespar:
        m,a,b = gcd_extendido_binario(x//2, y//2)
        m *= 2
    elif xespar:
        m,a,b = gcd_extendido_binario(x//2, y)
        if a % 2 == 0:
           a //= 2
        else:
           a = (a+y)//2
           b = b - x//2
    elif yespar:
        m,a,b = gcd_extendido_binario(x, y//2)
        if b % 2 == 0:
           b //= 2
        else:
           b = (b+x)//2
           a = a - y//2
    elif x > y:
        m,a,b = gcd_extendido_binario(y, x-y)
        a,b = b,a-b
    else:
        m,a,b = gcd_extendido_binario(x, y-x)
        a -= b
    return m,a,b


def inverso_mod_n(a, n):
    gcd, x, y = gcd_extendido_binario(a, n)
    return x % n
    

def baby_step_giant_step(g, y, p, q_i):
    N = raiz_cuadrada_techo(q_i)
    bsteps = {}
    for j in range(N):
        bsteps[pow(g, j, p)] = j
        
    ginvN = inverso_mod_n(pow(g, N, p), p) #Después lo multiplicaremos sucesivamente por sí mismo, recorriendo las potencias de giant step.
    aux = y
    for i in range(N):
        if aux in bsteps:
            j = bsteps[aux]
            return i * N + j
        aux = (aux * ginvN) % p
    return None


def th_chino_resto(restos, modulos):
    x = 0
    M = 1
    for mod in modulos:
        M *= mod
    for i in range(len(restos)):
        Mi = M // modulos[i]
        invMi = inverso_mod_n(Mi, modulos[i])
        x += restos[i] * Mi * invMi
    return x % M


def log_pohlig_hellman_rapido(y, g, p, q):
    n = p - 1
    listax = []
    listamod = []
    for q_i in q:
        potencia = n // q_i
        g_i = pow(g, potencia, p)
        y_i = pow(y, potencia, p)
        #Implementamos la funcion auxiliar para calcular los x_i (y lo guardamos
        #en la lista)
        x_i = baby_step_giant_step(g_i, y_i, p, q_i)
        listax.append(x_i)
        listamod.append(q_i)
    #Una vez con toda la lista, y aplicando el algoritmo del Teorema Chino del Resto
    #hallamos la solución
    x = th_chino_resto(listax, listamod)
    
    return x

