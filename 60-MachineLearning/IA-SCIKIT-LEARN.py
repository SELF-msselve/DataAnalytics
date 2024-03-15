# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:26:14 2024

@author: RY09678
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

boston=datasets.load_boston()
print(boston)

print(boston.keys())

print(boston.DESCR)

x=boston.data[:,np.newaxis, 5]
print('Imprimo solo columna 5')
#print(x)

y=boston.target
#print(y)

plt.scatter(x,y)
plt.title('Numero de habitaciones')
plt.xlabel('Habitaciones')
plt.ylabel('Valor medio')
plt.show()

######### IMPLEMENTACION DE REGRESION LINEAL SIMPLE ############
from sklearn.model_selection import train_test_split

#Separacion de datos en entrenamiento y test
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=.2)

#Algoritmo a utilizar Lineal Regression
lr = linear_model.LinearRegression()

#Entrenamiento del modelo
lr.fit(xTrain, yTrain)

#Prediccion
yPred=lr.predict(xTest)

#Graficamos los datos predictivos
plt.scatter(xTest, yTest, color='green')
plt.plot(xTest, yPred, color='red', linewidth=3)
plt.title('Regresion lineal simple')
plt.show()


########## IMPLEMENTACION REGRESION LINEAL MULTIPLE ###########
#Se sacan 4 columnas de los datos.
xMulti=boston.data[:,5:8]
print(xMultiple)

#Se saca la columna resultado
yMulti=boston.target

#Separacion de datos de entrenamiento y test
xMultiTrain, xMultiTest, yMultiTrain, yMultiTest = train_test_split(xMulti, yMulti, test_size=0.2)

#Linear Regression es siempre igual, ya sea simple o multiple
lrMulti=linear_model.LinearRegression()

lrMulti.fit(xMultiTrain,yMultiTrain)
yMultiPred=lrMulti.predict(xMultiTest)


########## IMPLEMENTACION REGRESION LINEAL POLiNOMICA ###########
from sklearn.preprocessing import PolynomialFeatures

#Se define el grado del polinomio
polireg=PolynomialFeatures(degree=3)

#Se transforman los datos. Lo que hace esto es generar una nueva matriz con las x elevadas a 0, 1, 2,.. degree
xTrainPoli=polireg.fit_transform(xTrain)
xTestPoli=polireg.fit_transform(xTest)

#Con estas matrices ahora se trabaja con una regresion lineal
pr=linear_model.LinearRegression()
pr.fit(xTrainPoli, yTrain)
yPredPoli=pr.predict(xTestPoli)

#Separacion de datos en entrenamiento y test
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=.2)

#Graficamos los datos predictivos
plt.scatter(xTest, yTest, color='green')
plt.scatter(xTest, yPredPoli, color='red')
plt.title('Regresion lineal simple')
plt.show()

print(pr.score(xTrainPoli, yTrain))


########## IMPLEMENTACION DE K VECINOS MAS CERCANOS ###########
from sklearn.neighbors import KNeighborsClassifier

algoritmo = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
algoritmo.fit(xTrain, yTrain)
yPredVecino=algoritmo.predict(xTest)


