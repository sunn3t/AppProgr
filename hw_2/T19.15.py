class TraceMeta(type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                dct[attr_name] = cls.trace_method(attr_name, attr_value)
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def trace_method(name, method):
        def traced_method(*args, **kwargs):
            print(f"Виклик методу '{name}' з аргументами: {args[1:]}, {kwargs}")
            result = method(*args, **kwargs)
            print(f"Метод '{name}' повернув: {result}")
            return result
        return traced_method


class Person(metaclass=TraceMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Привіт, мене звуть {self.name}, мені {self.age} років."


class Student(Person):
    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def calculate_scholarship(self, performance):
        if performance >= 90:
            return self.scholarship
        elif performance >= 75:
            return self.scholarship * 0.8
        else:
            return self.scholarship * 0.5


if __name__ == "__main__":
    person = Person("Іван", 30)
    student = Student("Марія", 20, 2000)

    print(person.introduce())
    print(student.introduce())
    print(student.calculate_scholarship(85))
