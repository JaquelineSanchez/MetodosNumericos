# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 22:09:01 2021

@author: JAQUELINA SANCHEZ
Implementacion del metodo de punto fijo
"""

#Parametros iniciales m=1.21, p= 0.001, v =6.75
def funcionFR(x):
    return ((87/(0.552+(1.21/(x**(1/2)))))*((x*0.001)**(1/2))-6.75)

def funcionGR(x):
    return ((0.552*(x**(1/2))+1.21)/(87*(0.001**(1/2)))*6.75)

def errorA(actual,anterior):
    return ((actual-anterior)/actual)*100

def puntofijo(r,e,n):
    i =0
    actual = r
    while i < n:        
        gR = funcionGR(actual)
        fR = funcionFR(actual)
        error = errorA(gR,actual)
        print("i={i},r={r:.6f},g(r)={gR:.6f},f(r)={fR:.6f},error = {e:.6f}".format(r=actual,gR=gR,fR=fR,e=error,i=i))
        if error < e:
            print("Se ha encontrado una raiz en {0}".format(gR))
            break
        actual = gR
        i = i+1         
    
    
puntofijo(4,0.04,200)    