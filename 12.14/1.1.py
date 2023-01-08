import re

class TextParser:
    """Парсер текстовых данных в некой системе."""

    def __init__(self, text: str):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor) -> None:
        """Вызывает метод класса обработчика.
        :param processor: экземпляр класса обработчика
        """
        result = processor.process_text(self.text)
        print(*result, sep='\n')


class WordCounter:
    """Счётчик частотности слов в тексте."""

    def __init__(self, text: str) -> None:
        """Обрабатывает переданный текст и создаёт словарь с частотой слов."""
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word: str) -> int:
        """Возвращает частоту переданного слова."""
        return self.__words.get(word, 0)

    def get_all_words(self) -> dict[str, int]:
        """Возвращает словарь с частотой слов."""
        return self.__words.copy()


class Adapter:
    """Адаптер, позволяющий парсеру использовать метод(-ы) счётчика."""
    def __init__(self, adapt):
        self.adapt = adapt

    def process_text(self, txt):
        self.adapt.__init__(txt)
        dct = self.adapt.get_all_words()
        lst = sorted(dct, key=dct.__getitem__)

        return reversed(lst)

text = """
        Жил на свете Мальчик Петя,
        Мальчик Петя Пинчиков.
        И сказал он: Тётя, тётя,
        Дайте, тётя, Блинчиков.
        Но сказала тётя Пете:
        Петя, Петя Пинчиков!
        Не люблю я, когда дети
        Очень клянчут блинчиков.
       """

parser = TextParser(text)
counter = WordCounter('')
adapter = Adapter(counter)
parser.get_processed_text(adapter)

# Результат:

# тётя
# петя
# блинчиков
# пинчиков
# мальчик
# клянчут
# очень
# дети
# когда
# я
# люблю
# не
# пете
# сказала
# но
# дайте
# он
# сказал
# и
# свете
# на
# жил
