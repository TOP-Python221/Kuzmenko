class Options:
    """Шаблон Строитель для формирования текста кода класса с конструктором или без"""
    def __init__(self, name: str):
        self.name = name
        # ИСПОЛЬЗОВАТЬ: имена полей в отличие от имён методов не содержат глаголов
        self.__fields: dict = {}

    @property
    def add_field(self):
        return iter(self.__fields)

    @add_field.setter
    def add_field(self, argument: list):
        """Добавлять поля экземпляра в конструкторе"""
        self.__fields[argument[0]] = argument[1]

    # ИСПРАВИТЬ: аналогии — это замечательно, но только при уместности; какой цели в этой задаче служит выделение формирования строкового представления класса в отдельный защищённый метод?
    def __str(self) -> str:
        """Формирует текста кода класса"""
        space = ' '
        # УДАЛИТЬ: выражение не имеет смысла
        m = space * 0
        result = f"class {self.name}:"
        if self.__fields:
            # ИСПОЛЬЗОВАТЬ: следите за именами идентификаторов
            for name, value in self.__fields.items():
                # ИСПРАВИТЬ: кажется, вы невнимательно читаете текст задания и примеры
                result += f'\n{space*2}{name}: {value}'
        else:
            result += f'\n{space*2}pass'
        return result

    # ДОБАВИТЬ: в текстовое представление заголовок метода конструктора

    # КОММЕНТАРИЙ: в итоге, вы увеличиваете стек вызовов ни для чего
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

    def add_field(self,
                  name: str,
                  # ИСПОЛЬЗОВАТЬ: в value может быть передан любой тип
                  value=None) -> 'ClassBuilder':
        self.root.add_field = [name, value]
        return ClassBuilder(self.root)

    def __str__(self):
        return self.root.__str__()


cb = ClassBuilder('Person')
print(cb)

print('-'*20)

cb = ClassBuilder('Person').add_field('name', 'Alan').add_field('age', 24).add_field('sex', 'm')
print(cb)


# ДОБАВИТЬ: закомментированный вывод в результате выполнения


# ИТОГ: невнимательный разработчик – это несчастный разработчик — 5/8
