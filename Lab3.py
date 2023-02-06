from random import randint
from faker import Faker
fake = Faker("ru_RU")


class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = None
        self._author = None
        self.set_name(name)
        self.set_author(author)

    def __str__(self):
        return f"Книга: {self._name}. Автор: {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    def set_name(self, name: str) -> None:
        """
        Метод для задания названия книги.
        :param name: Название книги
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError(f"Введённое имя: '{name}' не str")
        self._name = name

    def set_author(self, author: str) -> None:
        """
        Метод для задания автора книги.
        :param author: Автор книги
        :return: None
        """
        if not isinstance(author, str):
            raise TypeError(f"Введённое название книги: '{author}' не str")
        self._author = author

    @staticmethod
    def init_int(digit: int) -> int:
        """
        Статический метод проверяет входной параметр на число класса int
        :param digit: Входной параметр
        :return: Входной параметр
        """
        if not isinstance(digit, int):
            raise TypeError(f"Параметр {digit} не int")
        return digit

    def random_book(self) -> None:
        """
        Метод для задания случайной книги.
        :return: None
        """
        self._name = ' '.join(fake.words(randint(1, 5))).title()
        self._author = fake.name()

class PaperBook(Book):
    """Книга в печатном формате."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = 0
        self.pages = self.init_int(pages)

    def __str__(self):
        return f"{super().__str__()}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"

    def random_paperbook(self) -> None:
        """
        Метод наследованый от random_book + задание случаного количества страниц.
        :return: None
        """
        super().random_book()
        self.pages = randint(1, 1000)

    def divination_book(self, page: int) -> str:
        """
        Метод для гадания по заданной странице в книге.
        :param page: Страница книги, int
        :return: Строчка книги, str
        """
        if page not in range(self.pages+1):
            print(f"В книге нет {page} страниц, выберите другую")
        print(f"Гадание по книге '{self._name}':")
        return ' '.join(fake.words(1)).title() + ' ' + ' '.join(fake.words(randint(1, 21))) + '.'


class AudioBook(Book):
    """Книга в аудио формате."""
    def __init__(self, name: str, author: str, duration: int):
        super().__init__(name, author)
        self.duration = 0
        self.duration = self.init_int(duration)
        self.reading_time = 0

    def __str__(self):
        return f"{super().__str__()}. Длительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"

    def random_audiobook(self) -> None:
        """
        Метод наследованый от random_book + задание случаной длины аудиокниги.
        :return: None
        """
        super().random_book()
        self.duration = randint(1, 600)

    def play(self, time_: int) -> print:
        """
        Метод для прослушивания time_ времени аудиокниги.
        :param time_: Время прослушивания
        :return: print времени затраченного на прочтение time_ и оставшегося времени прослушивания
        """
        if time_ > self.duration - self.reading_time:
            return print("Вы закончили слушать книгу.")
        self.reading_time += time_
        return print(f'Вы прослушали {self.reading_time}, осталось {self.duration - self.reading_time} минут(а)')

book = Book('', '')
book.random_book()
print(book)
book.set_name('Философия Платона')
print(book)
print("-------------------------------")

paperbook = PaperBook('', '', 1)
paperbook.random_paperbook()
print(paperbook)
print(paperbook.divination_book(5))
print("-------------------------------")

audiobook = AudioBook('', '', 0)
audiobook.random_audiobook()
print(audiobook)
audiobook.play(100)
audiobook.play(100)
