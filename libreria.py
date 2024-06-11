import numpy as np
import matplotlib.pyplot as plt

# Función para agregar flechas en los extremos
def add_arrows(ax, x_min, x_max):
    ax.annotate('', xy=(x_max, 0), xytext=(x_max - 0.5, 0),
                arrowprops=dict(arrowstyle="->", color='black'))
    ax.annotate('', xy=(x_min, 0), xytext=(x_min + 0.5, 0),
                arrowprops=dict(arrowstyle="->", color='black'))

# Función para crear la gráfica
def plot_inequality_solution(a):
    x_min, x_max = -10, 10  # Definir el intervalo x
    threshold = (a - 5) / 3  # Resolver la inecuación 3x + 5 > a
    
    # Crear una figura y eje
    fig, ax = plt.subplots(figsize=(10, 2))
    
    # Graficar la recta numérica
    ax.plot([x_min, x_max], [0, 0], color='black')
    add_arrows(ax, x_min, x_max)
    
    # Agregar una línea vertical en x = threshold
    ax.axvline(x=threshold, color='red', linestyle='--', label=f'x = {threshold:.2f}')
    
    # Puntos que satisfacen la inecuación
    solution_points = np.linspace(threshold, x_max, 100)
    ax.scatter(solution_points, np.zeros_like(solution_points), color='blue', label=f'Puntos que satisfacen 3x + 5 > {a:.2f}')
    
    # Establecer límites y etiquetas del gráfico
    ax.set_xlim(x_min - 1, x_max + 1)
    ax.set_ylim(-0.5, 0.5)
    ax.set_yticks([])
    ax.set_xlabel('x')
    ax.legend()
    ax.set_title(f'Solución de la inecuación 3x + 5 > {a:.2f} en el intervalo [{x_min}, {x_max}]')
    
    plt.show()

# Función para evaluar la inecuación
def evaluate_inequality(a):
    x_min, x_max = -10, 10  # Definir el intervalo x
    threshold = (a - 5) / 3  # Resolver la inecuación 3x + 5 > a
    
    # Puntos que satisfacen la inecuación
    solution_points = np.linspace(threshold, x_max, 100)
    
    return solution_points
# Aqui hacemos algunas pruebas de la función
# aqui tengo los segundos cambios