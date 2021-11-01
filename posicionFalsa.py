# -*- coding:utf-8 -*-
"""
Created on Sun Sep 26 15:04:54 2021
Implementación del metodo de posicion falsa
@author: JAQUELINA SANCHEZ
"""
import math

def funcion(c):
    return (((9.8*56)/c)*(1-math.exp(-(c/56)*10))-35)

def obtenerXR(xU,xL):
    return (xU-((funcion(xU)*(xL-xU))/(funcion(xL)-funcion(xU))))

def errorA(anterior,actual):
    return (abs((actual-anterior)/(actual))*100)

def posicionFalsa(xl,xu,e,n):
    i=0
    actual = 0
    anterior = 0
    while i <= n:
        fxl = funcion(xl)
        fxu = funcion(xu)
        if (fxl*fxu < 0):
            xr = obtenerXR(xu, xl)
            fxr = funcion(xr)
            print("i = {i}, xl={xl:.6f}, xu={xu:.6f},f(xl) ={fxl:.6f}, f(xu)={fxu:.6f}, xr={xr:.6f},f(xr)={fxr:.6f}".format(xl=xl,xr = xr,xu=xu,fxl=fxl,fxu=fxu,fxr=fxr, i = i))
            if i > 0:
                actual = xr
                error = errorA(anterior,actual)
                print("Error: {:.6f}".format(error))
                if error < e:                    
                    print("Se encontro una raiz en {:.6f}".format(xr))
                    break
                else:
                    anterior = xr
            else:
                anterior = xr
            if fxl*fxr >= 0:
                xl = xr
            else:
                xu = xr
            i = i+1                    
        else:
            print("No hay una raiz en el intervalo dado.")
            break
        

posicionFalsa(14,16,10**(-5),100)    