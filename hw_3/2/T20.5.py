import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def f(x):
    return np.sin(x)


def lagrange_interpolation(xi, yi, x):
    n = len(xi)
    l = np.zeros_like(x)
    for i in range(n):
        t = np.ones_like(x)
        for j in range(n):
            if i != j:
                t *= (x - xi[j]) / (xi[i] - xi[j])
        l += yi[i] * t
    return l


k_values = np.arange(2, 6)

fig, ax = plt.subplots(figsize=(8, 6))
line_true, = ax.plot([], [], color='blue', label='sin(x)')
line_interp, = ax.plot([], [], color='red', label='PL(x)')
text_info = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, verticalalignment='top')
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Інтерполяція функції поліномом Лагранжа')
ax.legend()


def init():
    line_true.set_data([], [])
    line_interp.set_data([], [])
    text_info.set_text('')
    return line_true, line_interp, text_info


def animate(i):
    k = k_values[i]
    n = 2 ** k
    xi = np.linspace(0, 2 * np.pi, n + 1)
    yi = f(xi)

    x = np.linspace(0, 2 * np.pi, 1000)
    y_true = f(x)
    y_interp = lagrange_interpolation(xi, yi, x)

    line_true.set_data(x, y_true)
    line_interp.set_data(x, y_interp)
    text_info.set_text(f'k = {k}, n = {n}')
    return line_true, line_interp, text_info


anim = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=len(k_values), interval=1000, blit=True
)

anim.save('lagrange_interpolation.mp4', writer='ffmpeg')

plt.show()
