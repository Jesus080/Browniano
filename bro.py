import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
n_steps = 1000  # Número de pasos que tomará la partícula
step_size = 1  # Tamaño de cada paso

# Inicializar las posiciones (comienza en el origen [0, 0])
x_positions = np.zeros(n_steps)
y_positions = np.zeros(n_steps)

# Generar los pasos aleatorios
for i in range(1, n_steps):
    # Elegir un ángulo aleatorio entre 0 y 2π
    angle = np.random.uniform(0, 2 * np.pi)
    
    # Calcular el desplazamiento en x e y
    x_positions[i] = x_positions[i - 1] + step_size * np.cos(angle)
    y_positions[i] = y_positions[i - 1] + step_size * np.sin(angle)

# Graficar la trayectoria de la partícula
plt.figure(figsize=(8, 8))
plt.plot(x_positions, y_positions, lw=2, color='blue')
plt.scatter(x_positions[0], y_positions[0], color='green', label='Inicio', zorder=5)
plt.scatter(x_positions[-1], y_positions[-1], color='red', label='Final', zorder=5)
plt.title('Simulación del Movimiento Browniano en 2D')
plt.xlabel('Posición X')
plt.ylabel('Posición Y')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Asegura que los ejes tengan la misma escala
plt.show()
