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
        matrix[(r),(c)]=float(input("Elemento a["+str(r)+","+str(c)+"]: "))        
    vector[(r)]=float(input("b["+str(r)+"]:"))
print("\nLa matriz es:\n")
print(matrix)

#Hacer ceros debajo de la diagonal principal
for k in range (0,m):
    for r in range(k+1,m):        
            factor=(matrix[r,k]/matrix[k,k])
            vector[r]=vector[r]-(factor*vector[k])
            for c in range(0,n):
                matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])

#sustitución hacia atrás
x[m-1]=vector[m-1]/matrix[m-1,m-1]

#Desde m-2 hasta 0 decrementando en uno
for r in range(m-2,-1,-1):
    suma = 0    
    for c in range(0,n):
        suma= suma+matrix[r,c]*x[c]
    x[r]=(vector[r]-suma)/matrix[r,r]

print("\nResultado de la matriz de coeficientes")
print(matrix)

print("\nResultado del vector de terminos independientes")
print(vector)

print("\nValores de las variables: ")
print(x)

