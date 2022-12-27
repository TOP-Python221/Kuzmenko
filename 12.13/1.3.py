# ОТВЕТИТЬ: что такое ДЭ?
"""Моя ДЭ на основе уже реализованной на уроке формы HTML элемента и строителя элементов."""


# СДЕЛАТЬ: применить все исправления из предыдущей задачи

class HTMLTag:
    """
    Описывает HTML тег, который может содержать вложенные теги.
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = ''):
        self.name = name
        self.value = value
        self.__nested: list[HTMLTag] = []
        # КОММЕНТАРИЙ: проблема с таким решением, заключается в том, что со временем у соседних тегов эти списки будут пересекаться, а ссылки на одни и те же объекты будут множиться; например, если вы захотите какой-то тег удалить, то вам придётся перебрать все соседние теги и у каждого проитерировать все эти списки — это приговор для производительности
        self.__rollback: list[HTMLTag] = []
        # КОММЕНТАРИЙ: упорядочивать соседние теги должна структура более высокого порядка, чем один элемент — некий класс, который управляет созданием элементов

    @property
    def nested(self):
        """Возвращает неиндексируемый итератор по всем вложенным тегам."""
        return iter(self.__nested)

    @nested.setter
    def nested(self, value: 'HTMLTag'):
        """Добавляет вложенный тег к текущему."""
        self.__nested += [value]

    @property
    # ИСПРАВИТЬ: не думаю, что существует сколько-нибудь общепринятое значение для "rollback tag" или для "откатанного тега" — подумайте ещё над именами
    def rollback(self):
        """Возвращает неиндексируемый итератор по всем откатанным тегам."""
        return iter(self.__rollback)

    @rollback.setter
    def rollback(self, value: 'HTMLTag'):
        """Добавляет тег к текущему. Выходит из вложенного тега."""
        self.__rollback += [value]

    def __str(self, indent_level: int) -> str:
        """Рекурсивно формирует строку с текущим и всеми вложенными тегами. Немного измененный под данную ДЗ"""
        margin = ' '*indent_level * self.default_indent_spaces
        eol = ''
        result = f"{margin}<{self.name}>{self.value}"
        if self.__nested:
            for tag in self.__nested:
                result += '\n' + tag.__str(indent_level+1)
            eol = f'\n{margin}'
        result += f"{eol}</{self.name}>"
        if self.__rollback:
            for tag in self.__rollback:
                result += '\n' + tag.__str(indent_level)
        return result

    def __str__(self):
        return self.__str(0)

    # в данной реализации нецелесообразно "прятать" класс HTMLBuilder
    @staticmethod
    def create(name: str, value: str = ''):
        return HTMLBuilder(name, value)


class HTMLBuilder:
    """
    Предоставляет методы для пошаговой инициализации экземпляра HTMLTag.
    """
    def __init__(self, root: HTMLTag | str, value: str = ''):
        if isinstance(root, HTMLTag):
            self.root = root
        elif isinstance(root, str):
            self.root = HTMLTag(root, value)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')

    def nested(self, name: str, value: str = '') -> 'HTMLBuilder':
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега."""
        tag = HTMLTag(name, value)
        self.root.nested = tag
        return HTMLBuilder(tag)

    def sibling(self, name: str, value: str = '') -> 'HTMLBuilder':
        """Добавляет вложенный тег к текущему тегу и возвращает текущий строитель."""
        tag = HTMLTag(name, value)
        self.root.nested = tag
        return self

    # КОММЕНТАРИЙ: это хорошо, что вы попробовали добавить строителю подобное поведение, но конкретная реализация не слишком удачная — подумайте ещё
    def nested_2(self, name: str, value: str = '') -> 'HTMLBuilder':
        # ИСПРАВИТЬ: снова невнимательность — разве вы текущий строитель возвращаете?
        """Добавляет тег к текущему тегу выходя из вложенности и возвращает текущий строитель."""
        tag = HTMLTag(name, value)
        self.root.rollback = tag
        return HTMLBuilder(tag)

    def build(self) -> HTMLTag:
        return self.root


class CVBuilder:
    """Класс, описывающий HTML документ портфолио человека."""
    def __init__(self, full_name: str, age: str, profession: str, email: str):
        self.full_name = full_name
        self.age = age
        self.profession = profession
        self.email = email
        # ИСПРАВИТЬ: имена полей в отличие от имён методов не содержат глаголов
        self.add_educations: list = []
        self.add_projects: list = []
        self.add_contacts: dict = {}

    # ИСПРАВИТЬ: в условии задачи и примерах дано минимальное содержание необязательных разделов — его стоит реализовать
    def add_education(self, *args):
        self.add_educations += args
        return self

    def add_project(self, *args):
        # КОММЕНТАРИЙ: проблема с таким использованием произвольных наборов аргументов заключается в том, что использующий этот метод сможет передать что угодно, включая полную ерунду, и эта ерунда будет вами радостно добавлена в атрибуты, после чего отображена в HTML документе — вы должны постоянно искать баланс между строго ограниченной и полностью произвольной сигнатурой метода, и тем, как эта сигнатура используется в самом методе
        self.add_projects += args
        return self

    def add_contact(self, **kwargs):
        for k, v in kwargs.items():
            self.add_contacts[k] = v
        return self

    def build(self) -> HTMLTag:
        """Строит текст тегов в зависимости от того есть ли необязательные разделы."""
        # ИСПРАВИТЬ: что за тяга к имени res? вы пересмотрели роликов про "нацеленность на результат"?) буду называть вас Коучем, а пока дайте идентификатору смыслосодержащее имя: например, такие объекты часто называют root (корень), но здесь подойдет и html, и doc (документ)
        res = HTMLTag.create('html')
        # ИСПРАВИТЬ: это очень-очень ленивая сборка, вы проигнорировали требования о содержимом разделов и не реализовали даже минимальную вёрстку
        s = res.nested('head')\
               .sibling('title', f'{self.full_name}: портфолио')\
               .nested_2('body')\
               .nested('div')\
               .nested('h2', 'Обо мне')\
               .nested_2('p', f'Мне {self.age} года/лет я {self.profession}, мой email: {self.email}')
        if self.add_educations:
            s.nested_2('h2', 'Образование:')\
             .nested_2('p', f'{self.add_educations}')
        if self.add_projects:
            s.nested_2('h2', 'Мои проекты:')\
             .nested_2('p', f'{self.add_projects}')
        if self.add_contacts:
            s.nested_2('h2', 'Мои контакты:')\
             .nested_2('p', f'{self.add_contacts}')

        total = res.build()
        return total


cv1 = CVBuilder('Иванов Иван Иванович', "26", 'художник-фрилансер', 'ivv@abc.de')\
    .add_education('Д/сад', 'Средняя школа')\
    .add_project('Проект-1', 'Проект-2')\
    .add_contact(telegram='адрес')
print(cv1.build())


# ДОБАВИТЬ: закомментированный вывод в результате выполнения

# <html>
#   <head>
#     <title>Иванов Иван Иванович: портфолио</title>
#   </head>
#   <body>
#     <div>
#       <h2>Обо мне</h2>
#       <p>Мне 26 года/лет я художник-фрилансер, мой email: ivv@abc.de</p>
#       <h2>Образование:</h2>
        # КОММЕНТАРИЙ: уверены, что информация об образовании, о проектах, о контактах должна выводиться именно таким образом?
#       <p>['Д/сад', 'Средняя школа']</p>
#       <h2>Мои проекты:</h2>
#       <p>['Проект-1', 'Проект-2']</p>
#       <h2>Мои контакты:</h2>
#       <p>{'telegram': 'адрес'}</p>
#     </div>
#   </body>
# </html>


# ИТОГ: проработать все комментарии и доработать задачу — 4/8
