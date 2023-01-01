
"""Шаблон Строитель для формирования текста кода класса с конструктором или без"""

class Options:
    """Шаблон Строитель для формирования текста кода класса с конструктором или без"""
    def __init__(self, name: str):
        self.name = name
        self.__fields: dict = {}

    @property
    def add_field(self):
        return iter(self.__fields)

    @add_field.setter
    def add_field(self, argument: list):
        """Добавлять поля экземпляра в конструкторе"""
        self.__fields[argument[0]] = argument[1]

    def __str__(self):
        """Формирует текст кода класса"""
        margin = ' '
        result = f"class {self.name}:"
        result2 = result + f'\n{margin * 2}def __init__(self):'
        if self.__fields:
            for name, value in self.__fields.items():
                result2 += f'\n{margin * 4}{name}: {value}'
            result = result2
        else:
            result += f'\n{margin * 2}pass'
        return result



class ClassBuilder:
    """Предоставляет методы для пошаговой конструкции текста кода класса"""
    def __init__(self, root: Options | str):
        if isinstance(root, Options):
            self.root = root
        elif isinstance(root, str):
            self.root = Options(root)
        else:
            raise TypeError('use Options or str instance for root parameter')

    def add_field(self, name: str, value=None) -> "ClassBuilder":
        lst = [name, value]
        self.root.add_field = lst
        return ClassBuilder(self.root)

    def __str__(self):
        return self.root.__str__()


cb = ClassBuilder('Person')
print(cb)
print('-'*20)
cb = ClassBuilder('Person').add_field('name', 'Alan').add_field('age', 22.5).add_field('sex', 'm')
print(cb)
#
# Результат:

# class Person:
#   pass
# --------------------
# class Person:
#   def __init__(self):
#     name: Alan
#     age: 2.5
#     sex: m
