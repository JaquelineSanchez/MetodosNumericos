# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 09:35:38 2021
Implementacion del metodo de Newton raphson
multivariable
@author: JAQUELINE SANCHEZ
"""

from tabulate import tabulate
import numpy as np
import math

#encontrar la diferencia vectorial
def dV(xA,xP,yA,yP,zA,zP):
    return math.sqrt((xA-xP)**2+(yA-yP)**2+(zA-zP)**2)

def F(x1,x2,x3):
    f1 = x1**2+2*x2**2+math.exp(x1+x2)+x1*x3-6.1718
    f2 = 10*x2+x2*x3
    f3 = math.sin(x1*x3)+x2**2+x1-1.141
    return np.matrix([[-f1],[-f2],[-f3]])

def Jacobiana(x1,x2,x3):
    J = np.matrix([[2*x1+math.exp(x1+x2)+x3,4*x2+math.exp(x1+x2),x1],[0,10+x3,x2],[x3*math.cos(x1*x3)+1,2*x2,x1*math.cos(x1*x3)]])
    Jinv = np.linalg.inv(J)
    return [J,Jinv]

def NewtonRaphson(x,y,z,e,n):
    print("\t\t Iniciando método de Newton Raphson multivariable sin convergencia")
    i = 0
    lista = []
    xP = x
    yP = y
    zP = z
    while i < n:
        f = F(xP,yP,zP)        
        J, Jinv = Jacobiana(xP,yP,zP)
        h = np.dot(Jinv,f)
        xA = xP + h[0,0]
        yA = yP + h[1,0]
        zA = zP + h[2,0]
        distancia = dV(xA,xP,yA,yP,zA,zP)        
        lista.append([i,round(xP,6),round(yP,6),round(zP,6),round(distancia,6)])            
        if(distancia < e):
            print(tabulate(lista, headers=["i", "x1", "x2", "x3", "dv"]))
            print("El metodo converge a raices: x1 = "+ str(round(xA,6))+";x2 = "+ str(round(yA,6))+"; x3 = "+str(round(zA,6))+".")
            break;
        xP = xA
        yP = yA
        zP = zA
        i = i+1
    
NewtonRaphson(1,1,1,0.33,20)    