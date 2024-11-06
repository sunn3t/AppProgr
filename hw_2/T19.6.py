def trace_methods(cls):
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            setattr(cls, attr_name, trace_method(attr_value))
    return cls


def trace_method(method):
    def wrapper(*args, **kwargs):
        print(f"Викликається метод '{method.__name__}' з параметрами: {args[1:]}, {kwargs}")
        result = method(*args, **kwargs)
        print(f"Метод '{method.__name__}' повернув: {result}")
        return result
    return wrapper


@trace_methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"


@trace_methods
class Student(Person):
    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def calculate_scholarship(self, grades):
        average_grade = sum(grades) / len(grades)
        if average_grade > 85:
            return f"Стипендія: {self.scholarship}"
        else:
            return "Стипендія не нарахована"

    def get_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Стипендія: {self.scholarship}"


person = Person("Андрій", 45)
print(person.get_info())

student = Student("Марія", 20, 1500)
print(student.get_info())

grades = [90, 85, 88, 92]
print(student.calculate_scholarship(grades))

