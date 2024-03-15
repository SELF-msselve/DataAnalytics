# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:50:30 2024

@author: RY09678
"""
import numpy as np
import pandas as pd

datos=np.array([['','col1','col2'],['fila1',11,22],['fila2',33,44]])
print(datos)

df=pd.DataFrame(data=datos[1:,1:], index=data[1:,0],columns=data[0, 1:])
print(df)

df1=pd.DataFrame(data=[[1,2,3,4],[5,6,7,8],[9,10,11,12]], index=['fila1','fila2','fila3'],columns=['col1','col2','col3','col4'])
print(df1)

print(df1.shape)
print(len(df1.index))
print(len(df1.columns))
print(df1.describe())


#isnull genera una matriz nueva bool True si el dato es nulo
print(df1.isnull())

"""
pd.dropna()  elimina la fila que tenga algun valor nulo

pd.dropna(axis=1) elimina las columnas que tengan algun valor nulo

pd.fillna(xx) Reemplaza valores nulos por xx en cada celda

pd.fillna(df1.mean()) Reemplaza todos los valores por el promedio

