# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 12:43:53 2021
Implementacion del metodo gauss Seidel 
para sistemas de ecuaciones lineales
"""

import numpy

tol = 0.1  #Nivel de tolerancia para EA
itera = 20;        #Numero de iteraciones maximas
m = int(input('Valor de m:'))
n = m

matrix = numpy.zeros((m,n))
#Cuando no nos dan valores iniciales especificos 
x=numpy.zeros((m))
#Cuando si dan valores iniciales
#x[0] = 3.11
#x[1] =-3.11
#x[2] = -7.11
#x[3] = -89.15
#print(x)

vector = numpy.zeros((n))
antes = numpy.zeros((m))

def errorA(actual,anterior):
    return abs((actual-anterior)/actual)*100
    

print ('Método de Gauss-Seidel')

#Revisar que sea estrictamente dominante
def esDominante(matriz):
    for i in range(0, n):
        suma = 0
        for j in range(0, m):
            if(i != j):
                suma = suma + matriz[i][j]
        if(matriz[i][i] < suma):
            return False
    return True

def hacerDom(matriz):
    for i in range(0, n):
        for j in range(0, n):
            if(abs(matriz[i][j]>abs(matriz[i][i]))):
                z = i
                for i in range(0, n):
                    aux = matriz[i][z]
                    matriz[i][z]=matriz[i][j]
                    matriz[i][j]=aux
                    
        
    
#Introducir matriz
print ('Introduce la matriz de coeficientes y el vector solución')
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Elemento a["+str(r)+str(c)+"]: "))
    vector[(r)]=float(input('b['+str(r)+']: '))
print ("Matriz a procesar:")
print(matrix)


#Metodo de gauss Seidel
k=0
while k < itera:
    suma=0
    k=k+1
#Modificar el valor al requerido, lamda = 1 sirve cuando no se necesitan raices pesadas    
    lamda = 1   
    error = 0
    print("\n\tIteracion {}:".format(k))
    for r in range(0,m):
        suma=0
        for c in range(0,n):
            if (c != r):
                suma=suma+matrix[r,c]*x[c]               
        x[r]=(vector[r]-suma)/matrix[r,r] #Despeje
        print("x{num} = {v:.6f}".format(num=r,v=x[r]))    
        if(k > 1):                    
            x[r] = lamda*x[r]+(1-lamda)*antes[r]
            error = errorA(x[r],antes[r])
            print("Error absoluto de x{i} = {e:.6f}".format(i=r,e=error))            
            #Cuando solo se aplica el error a una variable especifica
            if(r == m-1):
                if(error < tol):
                    k = 21                
                    break
        antes[r] = x[r]
        
        
    