class Options:
    """Шаблон Строитель для формирования текста кода класса с конструктором или без"""
    def __init__(self, name: str):
        self.name = name
        self.__add_fields: dict = {}

    @property
    def add_field(self):
        return iter(self.__add_fields)

    @add_field.setter
    def add_field(self, argument: list):
        """Добавлять поля экземпляра в конструкторе"""
        self.__add_fields[argument[0]] = argument[1]

    def __str(self) -> str:
        """Формирует текста кода класса"""
        margin = ' '
        m = margin * 0
        result = f"{m}class {self.name}:"
        if self.__add_fields:
            for v, n in self.__add_fields.items():
                result += f'\n{margin * 2}{v}: {n}'
        else:
            result += f'\n{margin * 2}pass'
        return result

    def __str__(self):
        return self.__str()


class ClassBuilder:
    """Предоставляет методы для пошаговой конструкции текста кода класса"""
    def __init__(self, root: Options | str):
        if isinstance(root, Options):
            self.root = root
        elif isinstance(root, str):
            self.root = Options(root)
        else:
            raise TypeError('use Options or str instance for root parameter')

    def add_field(self, name: str, value: str|int = None) -> "ClassBuilder":
        lst = [name, value]
        self.root.add_field = lst
        return ClassBuilder(self.root)

    def __str__(self):
        return self.root.__str__()


cb = ClassBuilder('Person')
print(cb)
print('-'*20)
cb = ClassBuilder('Person').add_field('name', 'Alan').add_field('age', 24).add_field('sex', 'm')
print(cb)

