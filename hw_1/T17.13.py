def to_dense_matrices(func):
    def wrapper(matrix_a, matrix_b):
        matrix_a_dense = to_dense(matrix_a)
        matrix_b_dense = to_dense(matrix_b)
        return func(matrix_a_dense, matrix_b_dense)

    return wrapper


def to_dense(matrix):
    if isinstance(matrix, dict):
        rows = matrix.get('rows', 0)
        cols = matrix.get('cols', 0)
        dense_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for (i, j), value in matrix.get('values', {}).items():
            dense_matrix[i][j] = value
        return dense_matrix
    elif isinstance(matrix, list):
        return matrix


@to_dense_matrices
def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result

# Тестування
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

sparse_matrix = {
    'rows': 3,
    'cols': 3,
    'values': {
        (0, 0): 1,
        (1, 1): 5,
        (2, 2): 9
    }
}

print("Додавання густих матриць:")
print(add_matrices(matrix_a, matrix_b))

print("\nДодавання густої та розрідженої матриці:")
print(add_matrices(matrix_a, sparse_matrix))
