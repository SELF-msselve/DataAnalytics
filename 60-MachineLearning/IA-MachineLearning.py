# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 16:59:12 2024

@author: RY09678
"""

import numpy as np

#Matriz unidemncional
a = np.array([1,2,3])
print(a)

#Matriz 2D
b=np.array([(1,2,3),(4,5,6)])
print(b)

#Matriz con Onos.
unos=np.ones((3,4))
print(unos)
#Matriz con 0
ceros=np.zeros((3,4))
print(ceros)
#Matriz Random
aleatorios=np.random.random((3,4))
print(aleatorios)
#Matriz vacia
vacia=np.empty((2,4))
print(vacia)
#Matriz llena
full=np.full((2,2), 8)
print(full)
#linealmente distribuidas
#empieza en 0, termina en 50 saltando de a 5
espacio1=np.arange(0,50,5)
print(espacio1)
#empieza en 0, termina en 2, pone 20 numeros equidistantes
espacio2=np.linspace(0,2,20)
print(espacio2)

#Matrices Identidad
identidad1=np.eye(4,4)
print(identidad1)

identidad2=np.identity(4)
print(identidad2)

#Dimencionde una matriz
print(identidad2.ndim)

print(identidad2.dtype)

print(identidad2.size)
print(identidad2.shape)

#Transponer una matriz
c=np.array([(4,5,6,7),(8,9,10,11)])
fila, columna=c.shape

d=c.reshape(columna,fila)
print(c)
print(d)
print(c[0:,1])

print(c.min())
print(c.max())
print(c.sum())

