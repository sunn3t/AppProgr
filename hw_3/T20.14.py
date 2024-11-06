import numpy as np
from itertools import combinations

n = int(input("Уведіть кількість точок на площині, і потім одразу координати точок "))

arrPoints = np.empty((n, 2), dtype=int)
for i in range(n):
    arrPoints[i] = list(map(int, input().split()))

arrDist = np.empty(n, dtype=int)
maxPer = 0
triangle_indices = (0, 0, 0)

for i, j, k in combinations(range(n), 3):
    d_ij = np.sqrt((arrPoints[j][0] - arrPoints[i][0]) ** 2 + (arrPoints[j][1] - arrPoints[i][1]) ** 2)
    d_jk = np.sqrt((arrPoints[k][0] - arrPoints[j][0]) ** 2 + (arrPoints[k][1] - arrPoints[j][1]) ** 2)
    d_ki = np.sqrt((arrPoints[i][0] - arrPoints[k][0]) ** 2 + (arrPoints[i][1] - arrPoints[k][1]) ** 2)

    per = d_ij + d_jk + d_ki


    if per > maxPer:
        maxPer = per
        triangle_indices = (i, j, k)

print(f"Максимальний периметр: {maxPer}")
print(f"Індекси точок з максимальним периметром: {triangle_indices[0] + 1}, {triangle_indices[1] + 1}, {triangle_indices[2] + 1}")
