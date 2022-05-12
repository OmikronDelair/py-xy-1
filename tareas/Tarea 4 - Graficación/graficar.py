import numpy as np
import matplotlib.pyplot as plt

print("Crear una gráfica con números del 1 al 10 con intervalos de .1 usando un arreglo")

list = np.arange(1,10.1,.1)

plt.scatter(list,list)