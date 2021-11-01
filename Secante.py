# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:10:10 2021
Implementacion del metodo de la secante
@author: JAQUELINA SANCHEZ
"""

def funcionFX(x):
    return (x**4-6.4*(x**3)+6.45*(x**2)+20.538*x-31.752)

def funcionGX(actual,anterior):    
    fActual = funcionFX(actual)
    fAnterior = funcionFX(anterior)    
    return (actual-(fActual*(actual-anterior))/(fActual-fAnterior))

def errorA(actual,anterior):
    return abs((actual-anterior)/actual)*100

def criterioConvergencia(derivada):    
    if abs(derivada) < 1:
        return True
    else:
        return False

def Secante(ant,xi,e,n):
    print("\t\t Iniciando método de la secante")        
    i =0
    actual = xi
    anterior = ant
    while i < n:                
        fXi = funcionFX(actual)
        fAnterior = funcionFX(anterior)
        gX = funcionGX(actual,anterior)
        error = errorA(gX,actual)
        print("i={i},xi-1={xAnt:.7f},xi={xi:.7f},f(xi-1)={fXant:.7f},f(xi)={fxi:.7f},g(xi)={gxi:.7f},error = {e:.7f}".format(xAnt=anterior,fXant=fAnterior,fxi=fXi,xi=actual,gxi=gX,e=error,i=i))
        if error < e:
            print("Se ha encontrado una raiz en {0:.7f}".format(gX))
            break
        anterior = actual
        actual = gX        
        i = i+1         

Secante(0.65,1.3,0.1,200)
