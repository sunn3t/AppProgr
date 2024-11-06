import numpy as np
import matplotlib.pyplot as plt

n_max = 1000
n = np.arange(1, n_max + 1)
an = n**(1/n)

b = 1
epsilon = 0.05

condition = np.abs(an - b) < epsilon
k = np.argmax(condition)

plt.figure(figsize=(10, 6))

plt.plot(n, an, label='$a_n = n^{1/n}$', color='blue')
plt.axhline(y=b, color='green', linestyle='--', label='$y = b = 1$')
plt.fill_between(n, b - epsilon, b + epsilon, color='yellow', alpha=0.3, label='b - epsilon < a_n < b + epsilon')

plt.scatter([k], [an[k]], color='red', zorder=5)
plt.axvline(x=k, color='red', linestyle=':', label=f'$k = {k}$')


plt.xlabel('$n$')
plt.ylabel('$a_n$')
plt.title('Послідовність $a_n = n^{1/n}$ та її границя')
plt.legend()
plt.grid()
plt.ylim(0.9, 1.1)

plt.show()
