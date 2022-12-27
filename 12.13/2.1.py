from random import choice


class FilmCard:
    """Формируется базовый класс фильма."""
    def __init__(self, genre: str, title: str, year: int):
        self.genre = genre
        self.title = title
        self.year = year

    def __str__(self):
        return f'Название: {self.title}' \
               f'\nГод выпуска: {self.year}' \
               f'\nЖанр: {self.genre}'


class FilmCardMaker(FilmCard):
    """Дочерний класс формирует базовый класс фильма и дополняет его."""
    def __init__(self, genre, title, year):
        super().__init__(genre, title, year)
        self.director = str
        self.actors = []
        self.certificate = str
        self.country = str

    def add_director(self, d: str):
        self.director = d
        return self

    def add_actors(self, *actors):
        self.actors += actors
        return self
    
    def add_certificate(self):
        self.certificate = f'+{str(choice([0, 12, 18]))}'
        return self
    
    def add_country(self, c: str):
        self.country = c
        return self

    def __str(self):
        return f'\nСтрана: {self.country}' \
               f'\nРежиссер: {self.director}' \
               f'\nАктеры: {self.actors}' \
               f'\nРейтинг: {self.certificate}'

    def maker(self):
        return f'{self}{self.__str()}'


film = FilmCardMaker('драма', 'Война и Мир', 1965)
factory = film.add_director('Бондарчук')
factory.add_certificate()
factory.add_actors('Тихонов', 'Бондарчук')
factory.add_country('Россия')
filmcard2 = factory.maker()

film2 = FilmCardMaker('Ужасы', 'Чужой', 1979)
factory = film2.add_director('Риддли Скотт')
factory.add_certificate()
factory.add_actors('Сигурни Уивер')
factory.add_country('США')
filmcard = factory.maker()

film3 = FilmCardMaker('Ужасы', 'Нечто', 1982)
factory = film3.add_director('Джон Карпентер')
factory.add_certificate()
factory.add_actors('Курт Рассел')
factory.add_country('США')
filmcard3 = factory.maker()

print(filmcard)
print()
print(filmcard2)
print()
print(filmcard3)


# stdout:

# Название: Чужой
# Год выпуска: 1979
# Жанр: Ужасы
# Страна: США
# Режиссер: Ридли Скотт
# Актеры: ['Сигурни Уивер']
# Рейтинг: +18
#
# Название: Война и Мир
# Год выпуска: 1965
# Жанр: драма
# Страна: Россия
# Режиссер: Бондарчук
# Актеры: ['Тихонов', 'Бондарчук']
# Рейтинг: +0
#
# Название: Нечто
# Год выпуска: 1982
# Жанр: Ужасы
# Страна: США
# Режиссер: Джон Карпентер
# Актеры: ['Курт Рассел']
# Рейтинг: +12

