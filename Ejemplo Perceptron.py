import numpy as np
from sklearn.linear_model import Perceptron

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([0, 0, 0, 1])

modelo = Perceptron()
modelo.fit(X, Y)

predicciones = modelo.predict(X)

print("Datos de entrada (X):")
print(X)
print("Salidas reales (Y):", Y)
print("Predicciones del modelo:", predicciones)