import random

# Matriz de transición (Probabilidades de cambio de clima)
# El índice 0 representa 'soleado' y el índice 1 representa 'nublado'
transitions = [
    [0.8, 0.2],  # Probabilidad de quedarse en 'soleado' y cambiar a 'nublado'
    [0.4, 0.6]   # Probabilidad de quedarse en 'nublado' y cambiar a 'soleado'
]

# Estado inicial (probabilidad inicial)
current_state = random.choice([0, 1])

def next_state():
    transition_probs = transitions[current_state]
    new_state = random.choices([0, 1], transition_probs)[0]
    return new_state

# Simulación de un modelo de Markov durante 10 días
num_days = 10
sequence = []

for _ in range(num_days):
    sequence.append("Soleado" if current_state == 0 else "Nublado")
    current_state = next_state()

print("Secuencia de clima predicha:")
print(sequence)
