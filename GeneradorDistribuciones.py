import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Parámetros de la distribución normal
mu, sigma = 0, 0.2  # media y desviación estándar
n = 1000  # número de valores a generar

# Generar valores aleatorios para la distribución normal
valores_normales = np.random.normal(mu, sigma, n)

# Crear un DataFrame para la distribución normal
df_normales = pd.DataFrame(valores_normales, columns=['Valor'])

# Guardar el DataFrame en un archivo CSV
df_normales.to_csv('valores_normales.csv', index=False)
print("CSV file 'valores_normales.csv' created successfully.")

# Graficar la distribución normal
plt.figure(figsize=(10, 6))
plt.hist(valores_normales, bins=30, density=True, alpha=0.6, color='g')
plt.title('Distribución Normal')
plt.ylabel('Densidad')
plt.xlabel('Valores')
plt.savefig('distribucion_normal.png')
plt.show()

# Parámetros de la distribución exponencial
exponencial = stats.expon()

# Generar valores aleatorios para la distribución exponencial
valores_exponenciales = exponencial.rvs(size=n)

# Crear un DataFrame para la distribución exponencial
df_exponenciales = pd.DataFrame(valores_exponenciales, columns=['Valor'])

# Guardar el DataFrame en un archivo CSV
df_exponenciales.to_csv('valores_exponenciales.csv', index=False)
print("CSV file 'valores_exponenciales.csv' created successfully.")

# Graficar la distribución exponencial
plt.figure(figsize=(10, 6))
plt.hist(valores_exponenciales, bins=30, density=True, alpha=0.6, color='b')
x = np.linspace(exponencial.ppf(0.01), exponencial.ppf(0.99), 100)
fp = exponencial.pdf(x)  # Función de Probabilidad
plt.plot(x, fp, 'r-', lw=2)
plt.title('Distribución Exponencial')
plt.ylabel('Densidad')
plt.xlabel('Valores')
plt.savefig('distribucion_exponencial.png')
plt.show()

# Parámetros de la distribución t de Student
df_t = 50  # grados de libertad
t_student = stats.t(df_t)

# Generar valores aleatorios para la distribución t de Student
valores_t_student = t_student.rvs(size=n)

# Crear un DataFrame para la distribución t de Student
df_t_student = pd.DataFrame(valores_t_student, columns=['Valor'])

# Guardar el DataFrame en un archivo CSV
df_t_student.to_csv('valores_t_student.csv', index=False)
print("CSV file 'valores_t_student.csv' created successfully.")

# Graficar la distribución t de Student
plt.figure(figsize=(10, 6))
plt.hist(valores_t_student, bins=30, density=True, alpha=0.6, color='m')
x = np.linspace(t_student.ppf(0.01), t_student.ppf(0.99), 100)
fp = t_student.pdf(x)  # Función de Probabilidad
plt.plot(x, fp, 'r-', lw=2)
plt.title('Distribución t de Student')
plt.ylabel('Densidad')
plt.xlabel('Valores')
plt.savefig('distribucion_t_student.png')
plt.show()