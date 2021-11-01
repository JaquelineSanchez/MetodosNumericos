# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:16:53 2021
Implementacion del metodo de biseccion
@author: JAQUELINE SANCHEZ
"""
import math

def funcion(x):                 #Funcion de la derivada
    valor = ((2.8*10**6)/((2.8*10**6)-(13.3*10**3)*x))
    return (2510*math.log(valor)-9.81*x-335)


def pm(a,b):            #Encontrar el punto medio del intervalo
    return ((a+b)/2)

def errorA(anterior,actual):
    return ((abs(actual-anterior))/actual)*100

# (a,b) intervalo inicial, e = error y n= iteracion maxima
def biseccion(a,b,e,n):    
    i = 0 
    actual = 0
    anterior = 0
    while i <= n:
        fA = funcion(a)
        fB = funcion(b)
        if (fA*fB < 0):
            pM = pm(a,b)
            fM = funcion(pM)
            print("i = {i}, a ={a:.6f}, b={b:.6f}, f(a)={fA:.6f}, f(b)={fB:.6f}, pM={pM:.6f},f(pM) = {fpM:.6f}".format(a=a,pM = pM,b=b,fA=fA,fB=fB,fpM=fM, i = i))
            if i > 0:
                actual = pM
                error = errorA(anterior,actual)
                print("Error: {:.6f}".format(error))
                if error < e:                    
                    print("Se encontro una raiz en {:.6f}".format(pM))
                    break
                else:
                    anterior = actual
            else:
                anterior = pM
            if fA*fM <= 0:
                b = pM
            else:
                a = pM
            i = i+1                    
        else:
            print("No hay una raiz en el intervalo dado.")
            break

    
biseccion(69,73,0.1,200)


    
