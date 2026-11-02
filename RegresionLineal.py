from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

california = fetch_california_housing(as_frame=True)
X = california.data['MedInc'].values[:50]
Y = california.target.values[:50]

X_reshape = X.reshape(-1, 1)

modelo = LinearRegression()
modelo.fit(X_reshape, Y)

Y_prediccion = modelo.predict(X_reshape)

plt.scatter(X, Y, color='blue', label='Datos reales')
plt.plot(X, Y_prediccion, color='red', linewidth=2, label='Regresion lineal')
plt.title('Ingreso Medio vs Valor de la Casa')
plt.xlabel('Ingreso Medio')
plt.ylabel('Valor de la Casa')
plt.legend()
plt.show()