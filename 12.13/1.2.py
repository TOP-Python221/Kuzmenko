"""Доработанный модуль builder1 класса HTML элемента и строителя с возможность добавления для каждого элемента (тега) произвольного количества атрибутов с именем и значением. Используется в качестве параметров соответствующих методов произвольный словарь аргументов **kwargs."""


class HTMLTag:
    """
    Описывает HTML тег (с атрибутами или без), который может содержать вложенные теги (с атрибутами или без).
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = '', **kwargs):
        self.name = name
        self.value = value
        self.__nested: list[HTMLTag] = []
        # УДАЛИТЬ: параметр kwargs используется только один раз и только в данном методе — нет смысла сохранять в атрибут
        self.arguments = kwargs
        r = []
        for k, v in self.arguments.items():
            # ИСПОЛЬЗОВАТЬ: конкатенация списков, хоть и пересоздаёт список, но при этом выполняется быстрее, чем метод append() — поэтому когда нет разницы между изменением и пересозданием объекта, лучше использовать конкатенацию
            r += [f' {k}: "{v}"']
        # ИСПРАВИТЬ: с самого начала привыкайте писать осмысленные имена переменных, атрибутов, функций, классов — любые идентификаторы, которые вы вводите в код, должны максимально недвусмысленно своим именем указывать на причину собственного существования — res подходит для имени временной переменной, а не для атрибута
        self.res = ', '.join(r)
        # ИСПОЛЬЗОВАТЬ: вообще, из-за такой ерунды разводить код на пять строчек — это расточительно
        self.attributes = ','.join(f' {k}: "{v}"' for k, v in kwargs.items())

    @property
    def nested(self):
        """Возвращает неиндексируемый итератор по всем вложенным тегам."""
        return iter(self.__nested)

    @nested.setter
    def nested(self, value: 'HTMLTag'):
        """Добавляет вложенный тег к текущему."""
        self.__nested += [value]

    def __str(self, indent_level: int) -> str:
        """Рекурсивно формирует строку с текущим и всеми вложенными тегами и их атрибутами."""
        margin = ' '*indent_level * self.default_indent_spaces
        eol = ''
        result = f"{margin}<{self.name}{self.attributes}>{self.value}"
        if self.__nested:
            for tag in self.__nested:
                result += '\n' + tag.__str(indent_level+1)
            eol = f'\n{margin}'
        result += f"{eol}</{self.name}>"
        return result

    def __str__(self):
        return self.__str(0)

    # в данной реализации нецелесообразно "прятать" класс HTMLBuilder
    @staticmethod
    def create(name: str, value: str = '', **kwargs):
        return HTMLBuilder(name, value, **kwargs)


class HTMLBuilder:
    """
    Предоставляет методы для пошаговой инициализации экземпляра HTMLTag.
    """
    def __init__(self, root: HTMLTag | str, value: str = '', **kwargs):
        if isinstance(root, HTMLTag):
            self.root = root
        elif isinstance(root, str):
            self.root = HTMLTag(root, value, **kwargs)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')

    def nested(self, name: str, value: str = '', **kwargs) -> 'HTMLBuilder':
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега."""
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested = tag
        return HTMLBuilder(tag)

    def sibling(self, name: str, value: str = '', **kwargs) -> 'HTMLBuilder':
        """Добавляет вложенный тег к текущему тегу и возвращает текущий строитель."""
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested = tag
        return self

    def build(self) -> HTMLTag:
        return self.root


# ДОБАВИТЬ: многие HTML теги используют атрибут class, а в python это слово является зарезервированным — как с помощью строителя создать экземпляр HTMLTag с атрибутом class?
root = HTMLTag.create('div', link='', href='https://journal.top-academy.ru/')
root.sibling('p', 'Menu', link='', href='https://journal.top-academy.ru/')\
    .nested('ul', link='')\
    .sibling('li', 'File')\
    .sibling('li', 'Edit', link='')\
    .sibling('li', 'View')
div = root.build()
print(div)


# ДОБАВИТЬ: закомментированный вывод в результате выполнения


# ИТОГ: хорошо — 3/4
