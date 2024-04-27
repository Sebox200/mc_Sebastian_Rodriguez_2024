# -*- coding: utf-8 -*-
"""Taller20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZtN3yl9pG84byhQfHPh0Qv9aZFP4JcZ7
"""

import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([0.1, 0.3, 0.9, 1.7, 2.8, 4.5, 6.9])

# Calculando la regresión lineal
slope, intercept = np.polyfit(x, y, 1)

# Calculando la predicción de y
y_pred = slope * x + intercept

# Calculando la desviación estándar de los residuos
residuals = y - y_pred
std_dev = np.std(residuals)

# Calculando el error estándar de la estimación
stderr_est = np.sqrt(np.sum(residuals**2) / (len(x) - 2))

# Calculando el coeficiente de determinación (r^2)
r_squared = 1 - (np.sum(residuals**2) / np.sum((y - np.mean(y))**2))

# Calculando el coeficiente de correlación (r)
correlation_coefficient = np.corrcoef(x, y)[0, 1]

# Imprimiendo los resultados
print("Desviación estándar:", std_dev)
print("Error estándar de la estimación:", stderr_est)
print("Coeficiente de determinación (r^2):", r_squared)
print("Coeficiente de correlación (r):", correlation_coefficient)

# Graficando la regresión
plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal')
plt.show()