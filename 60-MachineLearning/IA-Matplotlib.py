# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:59:46 2024

@author: RY09678
"""

import matplotlib.pyplot as plt

x1=[1,2,3,4]
y1=[11,12,13,14]
x2=[3,5,7,8,2]
y2=[34,54,23,43,12]


plt.plot(x1, y1, color='blue', linewidth=3, label='linea 1')
plt.plot(x2, y2, color='green', linewidth=3, label='linea 2')

plt.title('Diagrama de Lineas')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

plt.legend()
plt.grid()
plt.show


plt.bar(x1, y1, color='blue', linewidth=3, label='linea 1')
plt.bar(x2, y2, color='green', linewidth=3, label='linea 2')

plt.title('Diagrama de Lineas')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

plt.legend()
plt.grid()
plt.show
