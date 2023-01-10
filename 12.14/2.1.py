from abc import ABC, abstractmethod


# Passenger & Cargo Carriers
class Carrier(ABC):
    """Интерфейс для реализации различных видов перевозчиков"""
    @abstractmethod
    def carry_military(self, items):
        pass

    @abstractmethod
    def carry_commercial(self, items):
        pass


# Military & Commercial Planes
class Plane(ABC):
    """Интерфейс для реализации различных классов самолетов"""
    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def add_objects(self, new_objects):
        pass


class Passenger(Carrier):
    # ИСПРАВИТЬ: не "коммерческого", а "пассажирского"
    """Класс для реализации коммерческого типа самолета"""
    def carry_military(self, items: str):
        return f'На борту: {items}. Военная пассажирская перевозка.'

    def carry_commercial(self, items: str):
        return f'На борту: {items}. Коммерческая пассажирская перевозка.'


class Cargo(Carrier):
    # ИСПРАВИТЬ: просто "грузового"
    """Класс для реализации военного/грузового типа самолета"""
    def carry_military(self, items: str):
        return f'На борту: {items}. Военный груз.'

    def carry_commercial(self, items: str):
        return f'На борту: {items}. Коммерческий груз.'


class Military(Plane):
    """Класс военного типа самолёта."""
    def __init__(self, purpose: Carrier):
        self.__purpose = purpose
        self.__name = 'Военный самолет'
        self.objects: list = []

    def display_description(self):
        print(f'{self.__name}. {self.__purpose.carry_military(self.objects)}')

    def add_objects(self, new_objects: str):
        self.objects += [new_objects]
        return self


class Commercial(Plane):
    """Класс коммерческого типа самолёта."""
    def __init__(self, purpose: Carrier):
        # КОММЕНТАРИЙ: атрибуты __purpose и objects инициализируются одинаково для классов Military, Commercial и, вероятно, всех прочих потенциальных подклассов Plane — на такие моменты необходимо обращать внимание
        # ИСПРАВИТЬ здесь и выше: в таких случаях, целесообразно вынести их инициализацию в конструктор базового класса, вызывая конструктор родительского класса из каждого конструктора дочернего с помощью super().__init__(...)
        self.__purpose = purpose
        self.__name = 'Коммерческий самолет'
        self.objects: list = []

    def display_description(self):
        print(f'{self.__name}. {self.__purpose.carry_commercial(self.objects)}')

    def add_objects(self, new_objects: str):
        self.objects += [new_objects]
        return self


# ИСПРАВИТЬ здесь и далее: в Python для имён переменных принято использовать змеиный_нижний_регистр (snake_lower_case)
militaryPlane1 = Military(Passenger())
militaryPlane1.add_objects('Десантники')
militaryPlane1.display_description()

militaryPlane2 = Military(Cargo())
militaryPlane2.add_objects('Патроны').add_objects('Гранаты')
militaryPlane2.display_description()

commercialPlane1 = Commercial(Cargo())
commercialPlane1.add_objects('Продукты').add_objects('Медикаменты')
commercialPlane1.display_description()

commercialPlane2 = Commercial(Passenger())
commercialPlane2.add_objects('Пассажиры')
commercialPlane2.display_description()


# stdout:

# Военный самолет. На борту: ['Десантники']. Военная пассажирская перевозка.
# Военный самолет. На борту: ['Патроны', 'Гранаты']. Военный груз.
# Коммерческий самолет. На борту: ['Продукты', 'Медикаменты']. Коммерческий груз.
# Коммерческий самолет. На борту: ['Пассажиры']. Коммерческая пассажирская перевозка.


# ИТОГ: очень хорошо — 7/8
