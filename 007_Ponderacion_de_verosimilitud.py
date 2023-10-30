import numpy as np

# Estimaciones
estimacion_1 = 10.0
estimacion_2 = 12.0

# Varianzas
varianza_1 = 1.0
varianza_2 = 4.0

# Calcular las ponderaciones de verosimilitud
peso_1 = 1 / varianza_1
peso_2 = 1 / varianza_2

# Calcular la suma de los pesos
suma_pesos = peso_1 + peso_2

# Calcular la estimación ponderada de verosimilitud
estimacion_ponderada = (peso_1 * estimacion_1 + peso_2 * estimacion_2) / suma_pesos

print("Estimación ponderada de verosimilitud:", estimacion_ponderada)
