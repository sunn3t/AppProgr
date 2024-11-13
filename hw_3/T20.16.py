import numpy as np


def progr(matrix):
    max_elem = np.max(matrix, axis=1)
    elem = np.min(max_elem)
    return elem


n = int(input())
matrix = np.random.randint(10, size=(n, n))
print("Рандомна матриця:")
print(matrix)

result = progr(matrix)
print("\nНайменший з найбільших у кожному рядку:", result)
