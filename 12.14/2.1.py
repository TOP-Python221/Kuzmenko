from abc import ABC, abstractmethod

# Passenger & Cargo Carriers
class Carrier(ABC):
    "Интерфейс для реализации различный видов перевозчиков"
    @abstractmethod
    def carry_military(self, items):
        pass

    @abstractmethod
    def carry_commercial(self, items):
        pass


# Military & Commercial Planes
class Plane(ABC):
    "Интерфейс для реализации различный классов самолетов"
    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def add_objects(self, new_objects):
        pass


class Passenger(Carrier):
    "Класс для реализации коммерческого типа самолета"
    def carry_military(self, items: str):
        return f'На борту: {items}. Военная пассажирская перевозка.'

    def carry_commercial(self, items: str):
        return f'На борту: {items}. Коммерческая пассажирская перевозка.'


class Cargo(Carrier):
    "Класс для реализации военного/грузового типа самолета"
    def carry_military(self, items: str):
        return f'На борту: {items}. Военный груз.'

    def carry_commercial(self, items: str):
        return f'На борту: {items}. Коммерческий груз.'


class Military(Plane):
    "Класс военного типа самолета"
    def __init__(self, purpose: Carrier):
        self.__purpose = purpose
        self.__name = 'Военный самолет'
        self.objects: list = []

    def display_description(self):
        if self.__purpose == Passenger():
            print(f'{self.__name}. {self.__purpose.carry_military(self.objects)}')
        print(f'{self.__name}. {self.__purpose.carry_military(self.objects)}')

    def add_objects(self, new_objects: str):
        self.objects += [new_objects]
        return self

class Commercial(Plane):
    "Класс коммерческого типа самолета"
    def __init__(self, purpose: Carrier):
        self.__purpose = purpose
        self.__name = 'Коммерческий самолет'
        self.objects: list = []

    def display_description(self):
        if self.__purpose == Passenger():
            print(f'{self.__name}. {self.__purpose.carry_commercial(self.objects)}')
        print(f'{self.__name}. {self.__purpose.carry_commercial(self.objects)}')

    def add_objects(self, new_objects: str):
        self.objects += [new_objects]
        return self


militaryPlane1 = Military(Passenger())
militaryPlane1.add_objects('Десантники')
militaryPlane2 = Military(Cargo())
militaryPlane2.add_objects('Патроны').add_objects('Гранаты')
commercialPlane1 = Commercial(Cargo())
commercialPlane1.add_objects('Продукты').add_objects('Медикаменты')
commercialPlane2 = Commercial(Passenger())
commercialPlane2.add_objects('Пассажиры')

militaryPlane1.display_description()
militaryPlane2.display_description()
commercialPlane1.display_description()
commercialPlane2.display_description()

# Результат:

# Военный самолет. На борту: ['Десантники']. Военная пассажирская перевозка.
# Военный самолет. На борту: ['Патроны', 'Гранаты']. Военный груз.
# Коммерческий самолет. На борту: ['Продукты', 'Медикаменты']. Коммерческий груз.
# Коммерческий самолет. На борту: ['Пассажиры']. Коммерческая пассажирская перевозка.
