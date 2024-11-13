import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class DrunkardND:
    '''Клас, що реалізує випадковий шлях у N-вимірному просторі ("хода п'яниці").'''

    def __init__(self, num_drunkards, dimensions=2, init_pos=None, is_limited=False, bounds=None):
        self._n_d = num_drunkards  # кількість точок (молекул)
        self._dims = dimensions  # кількість вимірів
        self._is_limited = is_limited  # чи обмежена область
        self._bounds = bounds  # границі області
        self._pos = init_pos  # позиції всіх точок

        if self._pos is None:
            # Якщо позиції не задано, встановлюємо всі у нульові координати
            self._pos = np.zeros((self._dims, self._n_d))
            if self._is_limited and self._bounds is not None:
            # Якщо задано границі, встановлюємо всі точки у середину області
                mins = np.array(self._bounds[:self._dims])
                maxs = np.array(self._bounds[self._dims:])
                center = (mins + maxs) / 2
                self._pos += center.reshape(self._dims, 1)

        # Можливі рухи: в кожному вимірі -1, 0 або 1 (крім нульового вектора)
        self._dirs = []
        for dim in range(self._dims):
            dir_vector = np.zeros(self._dims)
            dir_vector[dim] = 1
            self._dirs.append(dir_vector)
            dir_vector_neg = np.zeros(self._dims)
            dir_vector_neg[dim] = -1
            self._dirs.append(dir_vector_neg)
        self._dirs = np.array(self._dirs).T  # Транспонуємо для зручності

    @property
    def bounds(self):
        '''Властивість границі (читання).'''
        return self._bounds

    @bounds.setter
    def bounds(self, new_bounds):
        '''Властивість границі (встановлення).'''
        self._bounds = new_bounds

    @property
    def pos(self):
        '''Властивість позиції точок (тільки читання).'''
        return self._pos

    def _push_into_bounds(self):
        '''Повернути всі точки у межі області.'''
        mins = np.array(self._bounds[:self._dims]).reshape(self._dims, 1)
        maxs = np.array(self._bounds[self._dims:]).reshape(self._dims, 1)
        self._pos = np.maximum(self._pos, mins)
        self._pos = np.minimum(self._pos, maxs)

    def step(self):
        '''Зробити один крок у моделюванні.'''
        # Масив індексів для вибору випадкового напрямку для кожної точки
        ids = np.random.randint(0, len(self._dirs.T), self._n_d)
        # Масив приростів чергового кроку
        dpos = self._dirs[:, ids]
        self._pos += dpos
        if self._is_limited and self._bounds is not None:
            self._push_into_bounds()

    def msteps(self, m):
        '''Зробити m кроків у моделюванні.'''
        for _ in range(m):
            self.step()

    def get_positions(self):
        '''Отримати поточні позиції точок.'''
        return self._pos.copy()

# Параметри моделювання
num_molecules = 500  # Кількість молекул кожного газу
num_steps = 10000  # Кількість кроків моделювання
bounds = [0, 0, 100, 100]  # Границі області: xmin, ymin, xmax, ymax

# Ініціалізація молекул газу A (лівий бік області)
init_pos_A = np.random.uniform(
    low=[bounds[0], bounds[1]],
    high=[bounds[2] / 2, bounds[3]],
    size=(num_molecules, 2)
).T
gas_A = DrunkardND(
    num_drunkards=num_molecules,
    dimensions=2,
    init_pos=init_pos_A,
    is_limited=True,
    bounds=bounds
)

# Ініціалізація молекул газу B (правий бік області)
init_pos_B = np.random.uniform(
    low=[bounds[2] / 2, bounds[1]],
    high=[bounds[2], bounds[3]],
    size=(num_molecules, 2)
).T
gas_B = DrunkardND(
    num_drunkards=num_molecules,
    dimensions=2,
    init_pos=init_pos_B,
    is_limited=True,
    bounds=bounds
)

# Підготовка для анімації
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(bounds[0], bounds[2])
ax.set_ylim(bounds[1], bounds[3])
ax.set_aspect('equal')
ax.set_title('Диффузія двох газів у двовимірному просторі')

# Початкові точки
scatter_A = ax.scatter(
    gas_A.pos[0], gas_A.pos[1],
    c='blue', label='Газ A', s=10
)
scatter_B = ax.scatter(
    gas_B.pos[0], gas_B.pos[1],
    c='red', label='Газ B', s=10
)

ax.legend()

def init():
    scatter_A.set_offsets(np.c_[gas_A.pos[0], gas_A.pos[1]])
    scatter_B.set_offsets(np.c_[gas_B.pos[0], gas_B.pos[1]])
    return scatter_A, scatter_B

def update(frame):
    gas_A.step()
    gas_B.step()
    scatter_A.set_offsets(np.c_[gas_A.pos[0], gas_A.pos[1]])
    scatter_B.set_offsets(np.c_[gas_B.pos[0], gas_B.pos[1]])
    return scatter_A, scatter_B

ani = animation.FuncAnimation(
    fig, update,
    frames=num_steps,
    init_func=init,
    blit=True,
    interval=100
)

# Збереження анімації у файл
ani.save('gas_diffusion.mp4', writer='ffmpeg', fps=10)

plt.show()

