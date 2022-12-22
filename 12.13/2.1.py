"""Не понял какой должен быть конечный результат (было бы не плохо имеет Пример, как в прошлых задачах)"""

class FilmCard:
    def __init__(self, genre: str,
                       year: int,
                       title: str,
                       director: str,
                       writer: str,
                       country: str,
                       duration: float,
                       certificate: str):
        self.genre = genre
        self.year = year
        self.title = title
        self.director = director
        self.writer = writer
        self.country = country
        self.duration = duration
        self.certificate = certificate

    def __str__(self):
        return f'{self.year}{self.director}{self.title}'


