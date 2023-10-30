import numpy as np

# Matriz de transición de la cadena de Markov
transition_matrix = np.array([
    [0.2, 0.8],
    [0.6, 0.4]
])

# Número de iteraciones del MCMC
num_iterations = 10000

# Estado inicial
current_state = 0

# Contador de visitas al estado 1
state_1_visits = 0

for _ in range(num_iterations):
    # Elegir el próximo estado basado en la matriz de transición
    next_state = np.random.choice([0, 1], p=transition_matrix[current_state])

    # Contar las visitas al estado 1
    if current_state == 1:
        state_1_visits += 1

    current_state = next_state

# Estimación de la probabilidad estacionaria
stationary_probability = state_1_visits / num_iterations

print("Estimación de la probabilidad estacionaria:", stationary_probability)
