import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k_values = np.arange(2, 10)
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_title('Наближення π за допомогою рівносторонніх n-кутників')

# Малювання кола
theta = np.linspace(0, 2 * np.pi, 1000)
x_circ = np.cos(theta)
y_circ = np.sin(theta)
ax.plot(x_circ, y_circ, color='blue', label='Коло')
polygon_line, = ax.plot([], [], color='red', label='n-кутник')

text_info = ax.text(-0.95, 0.95, '', fontsize=12, verticalalignment='top')


def init():
    polygon_line.set_data([], [])
    text_info.set_text('')
    return polygon_line, text_info


def animate(i):
    k = k_values[i]
    n = 2 ** k
    angles = np.linspace(0, 2 * np.pi, n + 1)
    x_polygon = np.cos(angles)
    y_polygon = np.sin(angles)
    polygon_line.set_data(x_polygon, y_polygon)

    side_length = 2 * np.sin(np.pi / n)
    perimeter = n * side_length
    pi_approx = perimeter / 2
    error = np.abs(np.pi - pi_approx)

    text_info.set_text(f'k = {k}\nn = {n}\nπ ≈ {pi_approx:.6f}\nПохибка = {error:.6e}')
    return polygon_line, text_info


anim = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=len(k_values), interval=1000, blit=True
)

ax.legend()
anim.save('pi_approximation.mp4', writer='ffmpeg')

plt.show()
