import random

def simulate_cerberus(queue, iterations=10000):
    """
    Simula el proceso de Cerberus mordiendo y calcula la probabilidad de escapar desde cada posición inicial.
    """
    escape_counts = {i: 0 for i in range(len(queue))}
    
    for _ in range(iterations):
        current_queue = queue[:]
        while current_queue:
            # Cerberus elige una cabeza al azar
            bite_index = random.randint(0, min(2, len(current_queue) - 1))
            escaped = current_queue.pop(bite_index)
            escape_counts[escaped] += 1
            
            # Avanzan las posiciones
            if not current_queue:
                break
            
            # Llenar los tres primeros si la fila lo permite
            if len(queue) > len(current_queue):
                current_queue.append(len(current_queue))
    
    # Calcular probabilidades
    return {pos: escape_counts[pos] / iterations for pos in escape_counts}

def find_best_position(n, iterations=10000):
    """
    Encuentra la mejor posición para maximizar la probabilidad de escapar.
    """
    queue = list(range(n))  # Crear la fila
    probabilities = simulate_cerberus(queue, iterations)
    best_position = max(probabilities, key=probabilities.get)
    return best_position, probabilities[best_position]

# Ejemplo de uso
n = 10  # Tamaño de la fila
iterations = 10  # Número de simulaciones
best_position, best_probability = find_best_position(n, iterations)
print(f"La mejor posición es: {best_position} con probabilidad de escapar: {best_probability:.4f}")
