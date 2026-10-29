import numpy as np
import matplotlib.pyplot as plt
# Oscar Flores NC = 1389
DiasX = ["Lun","Mar","Mie","Jue","Vie"]
Califa_va_Y = [5, 6, 3, 8, 10]

plt.bar(DiasX, Califa_va_Y)
plt.title('Califa en VA de Oscar Flores NC = 1389')
plt.xlabel("Dias semana habil0")
plt.ylabel("Calificaciones en VA")
plt.grid()
plt.show()