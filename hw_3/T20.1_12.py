import numpy as np
import matplotlib.pyplot as plt

n_max = 1000
n = np.arange(1, n_max + 1)
an = n**(1/n)

# Гіпотеза: границя b
b = 1

# Задане epsilon
epsilon = 0.05

# Перевірка існування такого k, для якого |a_m - b| < epsilon для всіх m > k
condition = np.abs(an - b) < epsilon
k = np.argmax(condition)  # Перший індекс, починаючи з якого виконується умова

# Побудова графіку
plt.figure(figsize=(10, 6))

# Графік послідовності a_n
plt.plot(n, an, label='$a_n = n^{1/n}$', color='blue')

# Пряма y = b
plt.axhline(y=b, color='green', linestyle='--', label='$y = b = 1$')

# Смуга (b - epsilon, b + epsilon)
plt.fill_between(n, b - epsilon, b + epsilon, color='yellow', alpha=0.3, label='b - epsilon < a_n < b + epsilon')

# Позначення точки k
plt.scatter([k], [an[k]], color='red', zorder=5)
plt.axvline(x=k, color='red', linestyle=':', label=f'$k = {k}$')

# Налаштування графіка
plt.xlabel('$n$')
plt.ylabel('$a_n$')
plt.title('Послідовність $a_n = n^{1/n}$ та її границя')
plt.legend()
plt.grid()
plt.ylim(0.9, 1.1)  # Масштаб осі y для ілюстрації границі

# Показати графік
plt.show()
