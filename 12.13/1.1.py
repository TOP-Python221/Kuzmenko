"""Шаблон Строитель для формирования текста кода класса с конструктором или без"""


# КОММЕНТАРИЙ: во время выполнения студентом работы над ошибками студент не удаляет комментарии преподавателя


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
        # УДАЛИТЬ: и зачем здесь "второй результат"? мало того, что ненужная переменная сама по себе путаницу вносит, так ещё и имя не несёт смысловой нагрузки
        # ИСПРАВИТЬ: наличие строки с заголовком конструктора точно также зависит от наличия полей, добавленных строителем
        result2 = result + f'\n{margin*2}def __init__(self):'
        if self.__fields:
            for name, value in self.__fields.items():
                # ИСПРАВИТЬ: так и не взяли на себя труд внимательно посмотреть пример на 29–32 строках в файле задачи? (см. комментарий к выводу)
                result2 += f'\n{margin*4}{name}: {value}'
            result = result2
        else:
            result += f'\n{margin*2}pass'
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
        # УДАЛИТЬ: переменные создаются в том случае, если объект, с которым ассоциирована переменная, используется больше одного раза — сколько раз в коде метода используется список [name, value]?
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


# stdout:

# class Person:
#   pass
# --------------------
# class Person:
#   def __init__(self):
      # КОММЕНТАРИЙ: вашей задачей является формирование строки, содержащей код объявления класса с методом-конструктором — в каком конструкторе вы видели такое объявление атрибутов экземпляра? строковые литералы без кавычек: если попробовать выполнить этот фрагмент, то интерпретатор будет уверен, что Alan и m — это переменные, причем использующиеся для аннотации (а не присвоения значений) локальных переменных (а не атрибутов) name, age и sex
#     name: Alan
#     age: 2.5
#     sex: m


# ИТОГ: не все исправления внесены, не все внесённые корректны, работаем дальше — 5/8


# КОММЕНТАРИЙ: подписи коммитов (commit message) также должны быть максимально информативны — берите пример с преподавателя
