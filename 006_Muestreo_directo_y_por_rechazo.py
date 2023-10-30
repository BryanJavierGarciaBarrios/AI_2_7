import random

# Generar 10 muestras aleatorias de una distribución uniforme en [0, 1]
samples = [random.uniform(0, 1) for _ in range(10)]

print("Muestras generadas por muestreo directo:")
print(samples)

import random
import math

# Función de densidad de probabilidad de la distribución objetivo (normal)
def target_distribution(x):
    return math.exp(-x**2 / 2) / math.sqrt(2 * math.pi)

# Función de densidad de probabilidad de la distribución auxiliar (exponencial)
def auxiliary_distribution(x):
    return 2 * math.exp(-2 * x)

samples = []
while len(samples) < 10:
    x = random.expovariate(2)  # Generar una muestra de la distribución auxiliar
    y = random.uniform(0, auxiliary_distribution(x))
    if y <= target_distribution(x):
        samples.append(x)

print("Muestras generadas por muestreo por rechazo:")
print(samples)
