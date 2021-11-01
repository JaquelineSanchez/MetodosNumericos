# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 22:09:01 2021

@author: JAQUELINA SANCHEZ
Implementacion del metodo de Newton Raphson
"""
import math

pi = math.pi

def funcionFX(x):
    return (pi*3*(x**2)-(pi/3)*(x**3)-75)

#derivada 1 de f(x)
def primerDerivada(x):
    return (2*pi*3*x-pi*(x**2))

#derivada 2 de f(x)
def segundaDerivada(x):
    return (2*pi*3-2*pi*x)

def funcionGX(x):
    funcion = funcionFX(x)
    derivada = primerDerivada(x)
    return (x-funcion/derivada)

def derivadaGX(x):
    funcion = funcionFX(x)
    segunda = segundaDerivada(x)
    primera = primerDerivada(x)
    return ((funcion*segunda)/(primera**2))

def errorA(actual,anterior):
    return abs((actual-anterior)/actual)*100

def criterioConvergencia(derivada):    
    if abs(derivada) < 1:
        return True
    else:
        return False

def NewtonRaphson(x,e,n):
    print("\t\t Iniciando método de Newton Raphson sin convergencia")
    #derivada = derivadaGX(x)
    #if criterioConvergencia(derivada):
    i =0
    actual = x
    while i < n:        
        gX = funcionGX(actual)
        fX = funcionFX(actual)
        derF1 = primerDerivada(actual)        
        error = errorA(gX,actual)
        print("i={i},h={x:.5f},f(h)={fX:.5f},f'(h)={fx1:.5f},g(h)={gx:.5f},error = {e:.7f}".format(x=actual,fx1=derF1,gx=gX,fX=fX,e=error,i=i))
        if error < e:
            print("Se ha encontrado una raiz en {0}".format(gX))
            break
        actual = gX
        i = i+1         
    #else:
        #print("No promete convergencia")
    
NewtonRaphson(4,0.0004,200)    