# Домашнее задание по теме "Интроспекция"


import inspect

def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__  # Получаем тип объекта в виде строки
    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__  # Проверка на наличие атрибута __module__
    else:
        info['module'] = 'N/A'  # Если атрибут отсутствует, записываем 'N/A'
    info['dir'] = dir(obj)  # Получаем список атрибутов и методов объекта
    return info


# Пример использования функции
number_info = introspection_info(42)
print(number_info)


# Для лучшего понимания создадим свой класс
class MyClass:
    def __init__(self, value):
        self.value = value
        self.name = "MyClass Instance"

    def display(self):
        return f"Value: {self.value}"


# Создаем экземпляр класса и получаем его информацию
my_instance_info = introspection_info(MyClass(10))
print(my_instance_info)



