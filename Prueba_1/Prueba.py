# Esto es un comentario

#Pandas es la librería básica para la manipulación y análisis de datos
import pandas as pd

#Numpy es la biblioteca para crear vectores y matrices, además de un conjunto grande de funciones matemáticas
import numpy as np

#Seaborn es una librería que usamos para graficar
import seaborn as sns

#Statsmodels es la biblioteca para realizar modelos
import statsmodels.formula.api as smf
#from cmath import pi


"""
c = "Hola"
d = "Mundo"
a = c + " " + d
print(a)
print("")
"""

a = "Hola"
a += " "
a += "Mundo"
print(a)
print("")


# Variable entero -> int
a = 4
print("Este es el numero " + str(a))
print("")

lv_pi = np.pi
print(lv_pi)
print(str(np.pi))
print("")

df_nations = pd.read_csv("Nations.csv", encoding="ISO-8859-1")
df_nations.drop(columns=["Unnamed: 0"], inplace = True)

print(df_nations.head())
print(chr(10) + chr(13))
print(df_nations.tail())
#print(df_nations['country'])

sns.displot(df_nations["gini"], kind="hist")
