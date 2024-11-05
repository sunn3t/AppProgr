def trace_recursive(func):
    depth = 0  # Лічильник глибини рекурсії

    def wrapper(*args, **kwargs):
        nonlocal depth
        indent = '  ' * depth
        print(f"{indent}Вхід у функцію '{func.__name__}' на рівні {depth}, з параметрами: {args}")

        depth += 1
        result = func(*args, **kwargs)
        depth -= 1

        print(f"{indent}Вихід з функції '{func.__name__}' на рівні {depth}, результат: {result}")
        return result

    return wrapper


@trace_recursive
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


@trace_recursive
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
k = int(input())

print(f"Факторіал числа {n}:")
factorial(n)

print(f"\nЧисло Фібоначчі для n = {k}:")
fibonacci(k)
