# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 22:09:01 2021

@author: JAQUELINA SANCHEZ
Implementacion del metodo de Newton Raphson
"""

def funcionFX(x):
    return (x**4-6.4*(x**3)+6.45*(x**2)+20.538*x-31.752)

#derivada 1 de f(x)
def primerDerivada(x):
    return (4*(x**3)-19.2*(x**2)+12.9*x+20.538)

#derivada 2 de f(x)
def segundaDerivada(x):
    return (12*(x**2)-38.4*x+12.9)

def funcionGX(x):
    funcion = funcionFX(x)
    primeraDer = primerDerivada(x)
    segundaDer = segundaDerivada(x)
    return (x-(funcion*primeraDer)/((primeraDer**2)-funcion*segundaDer))


def errorA(actual,anterior):
    return abs((actual-anterior)/actual)*100

def criterioConvergencia(derivada):    
    if abs(derivada) < 1:
        return True
    else:
        return False

def RalstonRabinowitz(x,e,n):
    print("\t\t Iniciando método de Ralston Rabinowitz")        
    i =0
    actual = x
    while i < n:        
        gX = funcionGX(actual)
        fX = funcionFX(actual)
        derF1 = primerDerivada(actual)
        derF2 = segundaDerivada(actual)        
        error = errorA(gX,actual)
        print("i={i},x={x:.7f},f(x)={fX:.7f},f'(x)={fx1:.7f},f''(x)={fx2:.7f},error = {e:.7f}".format(x=actual,fx1=derF1,fx2=derF2,fX=fX,e=error,i=i))
        if error < e:
            print("Se ha encontrado una raiz en {0:.7f}".format(gX))
            break
        actual = gX
        i = i+1         
    
RalstonRabinowitz(3.28,0.1,200)    