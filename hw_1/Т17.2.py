def funcResult(a, b):
    def myDecorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return max(a, min(b, result))
        return wrapper
    return myDecorator

a = int(input())
b = int(input())

@funcResult(a, b)
def func(x):
    return x

c = int(input())
print(func(c))
