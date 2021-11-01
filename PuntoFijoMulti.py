# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:00:54 2021
Implementación del metodo de punto fijo multivariable
@author: JAQUELINA SANCHEZ
"""

from tabulate import tabulate
from sympy import *
import math

#Definir variables
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

#Definir las g(x)
g1 = (1/3)*cos(y*z)+(1/6)
g2 = (1/9)*(x**2+sin(z)+1.06)**(1/2)-0.1
g3 = -(1/20)*exp(-x*y)-((10*pi-3)/60)
    
#Criterio de convergencia
def Criterio(v1, v2, v3):        
    #Sumar las derivadas parciales respecto de x de cada funcion g 
    pX = diff(g1,x).subs(x,v1)+diff(g2,x).subs(x,v1)+diff(g3,x).subs(x,v1)
    pX = pX.subs(y,v2)
    pX = pX.subs(z,v3)
    #Sumar las derivadas parciales respecto de y de cada funcion g 
    pY = diff(g1,y).subs(x,v1)+diff(g2,y).subs(x,v1) +diff(g3,x).subs(x,v1)
    pY = pY.subs(y,v2)
    pY = pY.subs(z,v3)
    #Sumar las derivadas parciales respecto de z de cada funcion g 
    pZ = diff(g1,y).subs(x,v1)+diff(g2,y).subs(x,v1) +diff(g3,x).subs(x,v1)
    pZ = pZ.subs(y,v2)
    pZ = pZ.subs(z,v3)    
    if(pX < 1 and pY < 1 and pZ < 1):
        return True
    return False

def funcionGX(vX,vY,vZ):
    nuevaX = g1.subs(x,vX)
    nuevaX = nuevaX.subs(y,vY)
    nuevaX = nuevaX.subs(z,vZ)
    return nuevaX
#   return (1/3)*math.cos(vY*vZ)+(1/6)

def funcionGY(vX,vY,vZ):
    nuevaY = g2.subs(x,vX)
    nuevaY = nuevaY.subs(y,vY)
    nuevaY = nuevaY.subs(z,vZ)
    return nuevaY
#   return (1/9)*math.sqrt(vX**2+sin(vZ)+1.06)-0.1

def funcionGZ(vX,vY,vZ):
    nuevaZ = g3.subs(x,vX)
    nuevaZ = nuevaZ.subs(y,vY)
    nuevaZ = nuevaZ.subs(z,vZ)
    return nuevaZ
#   return -(1/20)*math.exp(-vX*vY)-((10*math.pi-3)/60)

#encontrar la diferencia vectorial
def dV(xA,xP,yA,yP,zA,zP):
    return math.sqrt((xA-xP)**2+(yA-yP)**2+(zA-zP)**2)

def puntoFijo(X,Y,Z,e,n):
    i =0
    lista = []
    if(Criterio(X,Y,Z)):
        print("Si promete convergencia")
        xp = X
        yp = Y
        zp = Z
        while i<n:
            #print("i = "+str(i))
            xA = funcionGX(xp,yp,zp)            
            yA = funcionGY(xA,yp,zp)
            zA = funcionGZ(xA,yA,yp)
            distancia = dV(xA,xp,yA,yp,zA,zp)
            #print("x1 = "+ str(round(xA,5))+"; x2 = "+ str(round(yA,5))+"; x3 = "+str(round(zA,5))+"; dv ="+str(round(distancia,5)))
            lista.append([i,round(xp,5),round(yp,5),round(zp,5),round(distancia,5)])            
            if(distancia < e):
                #print(tabulate(lista, headers=["i", "x1", "x2", "x3", "dv"]))
                print("El metodo converge a raices: x1 = "+ str(round(xA,5))+";x2 = "+ str(round(yA,5))+"; x3 = "+str(round(zA,5))+".")
                break;
            xp = xA
            yp = yA
            zp = zA
            i = i+1
    else:
        print("No promete convergencia")
        
puntoFijo(0.1,0.1,-0.1,10**(-6),200)        

