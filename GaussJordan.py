# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:44:56 2021
Implementacion del metodo de eliminación gaussiana
para sistemas de ecuaciones
"""

import numpy

m = int(input('Valor de m:'))

n = m

#Crear la matriz de coeficientes
matrix = numpy.zeros((m,n))

#vector de terminos independientes
vector = numpy.zeros((n))
#Almacena los valores finales de las variables
x=numpy.zeros((m))

print("Introduce la matriz de coeficientes y el vector de terminos independientes")

for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Elemento a["+str(r)+","+str(c)+"]"))        
    vector[(r)]=float(input("b["+str(r)+"]:"))
print("\nLa matriz a desarrollar es:\n")
print(matrix)

#Hacer ceros debajo de la diagonal principal
for k in range (0,m):
    for r in range(0,m):
        if (r != k):
            factor=(matrix[r,k]/matrix[k,k])
            vector[r]=vector[r]-(factor*vector[k])
            for c in range(0,n):
                matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])
    

#Hacer 1s diagonal principal
for r in range(0,m):    
    x[r]=vector[r]/matrix[r,r]
    vector[r] = x[r]
    matrix[r,r]=matrix[r,r]/matrix[r,r]


print("\nResultado de la matriz de coeficientes")
print(matrix)

print("\nResultado del vector de terminos independientes")
print(vector)

print("\nValores de las variables: ")
print(x)

