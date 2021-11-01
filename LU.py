# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:20:17 2021
Implementacion de la descomposicion LU para 
resolver sistemas de ecuaciones
Fecha: 24/10/2021
@author: JAQUELINA SANCHEZ
"""

import numpy as np

print("\t\t\tMétodo de descomposición LU\n")
#Tamaño de la matriz mXm
m = int(input("Introduce el numero de renglones: "))

matriz = np.zeros([m,m])
u = np.zeros([m,m])
l = np.zeros([m,m])
d = np.zeros((m))
b = np.zeros((m))
x = np.zeros((m))

print("Introduce los elementos de la matriz de coeficientes y los terminos independientes")
for r in range(0,m):
    for c in range(0,m):
        matriz[r,c] = float(input("Elemento A["+str(r)+","+str(c)+"]: "))
        u[r,c] = matriz[r,c]
    b[r] = float(input("Elemento B["+str(r)+"]: "))
        
print("\nMatriz de coeficientes ingresada:")
print(matriz)
        
#Ceros debajo de la diagonal
for k in range(0,m):
    for r in range(0,m):
        #Lenar de 1s la diagonal de L
        if(k == r):
            l[k,r] = 1
        if(k < r):
            factor = u[r,k]/u[k,k]
            l[r,k]= factor            
            for c in range(0, m):
                u[r,c]=u[r,c]-(factor*u[k,c])

print("\nMatriz L:")
print(l)
print("\nMatriz U:")
print(u)
#Comprobar que la factorizacion este bien
a = np.dot(l,u) #L*U = A
#Comprobacion elemento a con elemento de matriz
if((a == matriz).all()):
    print("La factorizacion es correcta :D")
    
    #Sustitucion hacia adelante para encontrar D
    d[0] = b[0]
    for r in range(1, m):
        suma = 0
        for c in range(0,m):
            suma = suma + l[r,c]*d[c]
        d[r]=b[r]-suma
    print("\n Valor del vector D:")
    print(d)
    
    #Sustitucion hacia atras para encontrar X
    x[m-1]=d[m-1]/u[m-1,m-1]
    #Desde m-2 hasta 0 decrementando en uno
    for r in range(m-2,-1,-1):
        suma = 0    
        for c in range(0,m):
            suma= suma+u[r,c]*x[c]
        x[r]=(d[r]-suma)/u[r,r]
            
    print("\nValores de las incognitas obtenidos: ")
    print(x)
    
    print("Solución real aplicando inversa:")
    #Inversa de la matriz de coeficientes
    inversa = np.linalg.inv(matriz)
    #Resultado = Matriz inversa * vector de terminos independientes
    resultado = np.dot(inversa,b)
    print(resultado)
    
                