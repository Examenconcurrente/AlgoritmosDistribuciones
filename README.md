# Algoritmos de Distribuciones

Este repositorio contiene un conjunto de scripts en Python para generar y visualizar diferentes distribuciones estadísticas. El código se encuentra en el archivo `GeneradorDistribuciones.py`.

## Enlace al repositorio

[AlgoritmosDistribuciones](https://github.com/Examenconcurrente/AlgoritmosDistribuciones.git)

## Descripción del código

El script `GeneradorDistribuciones.py` realiza las siguientes tareas:

1. **Distribución Normal**:
   - Genera valores aleatorios siguiendo una distribución normal con media `mu` y desviación estándar `sigma`.
   - Guarda los valores generados en un archivo CSV (`valores_normales.csv`).
   - Grafica la distribución normal.

2. **Distribución Exponencial**:
   - Genera valores aleatorios siguiendo una distribución exponencial.
   - Guarda los valores generados en un archivo CSV (`valores_exponenciales.csv`).
   - Grafica la distribución exponencial.

3. **Distribución t de Student**:
   - Genera valores aleatorios siguiendo una distribución t de Student con `df_t` grados de libertad.
   - Guarda los valores generados en un archivo CSV (`valores_t_student.csv`).
   - Grafica la distribución t de Student.

## Requisitos

- Python 3.x
- Bibliotecas: `numpy`, `pandas`, `matplotlib`, `scipy`

## Gráficas

### Distribución Normal
![Distribución Normal](images/distribucion_normal.png)

### Distribución Exponencial
![Distribución Exponencial](images/distribucion_exponencial.png)

### Distribución t de Student
![Distribución t de Student](images/distribucion_t_student.png)