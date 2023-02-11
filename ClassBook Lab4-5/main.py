import re


class Book:
    def __init__(self, file):
        self.file = file
        self._data = []
        self.loader()
        self.cleaner()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    def __str__(self):
        return self.file.strip('txt')

    def loader(self) -> None:
        """
        Метод построчной загрузки файла книги формата txt в массив.
        :return: массив формата list со строками книги
        """
        with open(self.file, "r", encoding='utf-8') as f:
            for word in f:
                self.data.append(word)

    def cleaner(self) -> None:
        """
        Метод очистки строк книги от лишних символов
        :return: массив файла со строками книги
        """
        clear_data = []
        for str_ in self.data:
            if str_ not in ['\n']:
                for symb in ['\n', '\ufeff']:
                    str_ = str_.strip(symb)
                clear_data.append(str_)
        self.setter = clear_data  # TODO правильна ли эта запись?


class BackgroundChecks:

    @staticmethod
    def is_type(enter, type_):
        if not isinstance(enter, type_):
            raise TypeError(f"Введённое значение {enter} - не типа {type_}.")

    @staticmethod
    def in_range(enter, limit):
        if enter not in range(1, limit+1):
            raise ValueError(f"Выбранное значение не в пределах от 1 до {limit}")

    @staticmethod
    def ask_value(enter, type_):
        if enter is None:
            return type_(input(f"Вы не задали значение {type_}. Введите значение: "))
        else:
            return enter

class SearchInBook(Book, BackgroundChecks):
    def __init__(self, file):
        super().__init__(file)

    def getter_str(self, index: int) -> str:
        """
        Метод вызова строки по задаваемому параметру.
        :param index: номер вызываемой строки
        :return: вызываемая строка
        """
        self.is_type(index, int)
        return self.getter  # TODO правильна ли эта запись?

    def search_word(self, question=None) -> print:
        """
        Метод поиска слов по всей книге.
        :param question: искомое слово
        :return: количество совпадений
        """
        question = self.ask_value(question, str)
        self.is_type(question, str)
        question = question.lower()
        counter = 0
        for str_ in self.data:
            word_list = str_.split()
            for word in word_list:
                word = word.lower()
                result = re.match(f'{question}', word)
                if result:
                    counter += 1
        return f"Слово '{question}' найдено {counter} раз(а)."

    def how_many_str(self) -> str:
        """
        Метод для подсчёта количества строк в книге.
        :return: Количество строк в книге
        """
        return f"В книге {self.__str__()} - {len(self.data)} строк(и)."


class BookGames(SearchInBook):
    def __init__(self, file):
        super().__init__(file)

    def divination_by_book(self, question=None) -> print:
        """
        Метод для вызова предложения в задаваемой строке книги.
        :param question: Номер задаваемой строки
        :return: Предложение из задаваемой строки
        """
        question = self.ask_value(question, int)
        self.is_type(question, int)
        counter, sentence = 0, []
        str_ = self.getter_str(question).split('.')
        for text in str_:
            if text:
                counter += 1
            sentence.append(text)
        if counter == 1:
            return sentence[0] + '.'
        index = int(input(f'В указанной строчке {counter} предложения(ий). Введите № предложения от 1 до {counter}: '))
        self.in_range(index, counter)
        return sentence[index-1] + "."

if __name__ == '__main__':
    book = BookGames("Ф.М. Достоевский - Преступление и наказание.txt")
    book.divination_by_book(666)