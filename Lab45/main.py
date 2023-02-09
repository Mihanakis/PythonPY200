import re


class Book:
    def __init__(self, file):
        self._name = file.strip('txt')
        self.file = file
        self.data = []
        self.load_file_to_data_list()
        self.cleaner_data_list()

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.name = new_name

    def load_file_to_data_list(self) -> None:
        """
        Метод построчной загрузки файла книги формата txt в массив.
        :return: массив формата list со строками книги
        """
        with open(self.file, "r", encoding='utf-8') as f:
            for word in f:
                self.data.append(word)

    def cleaner_data_list(self) -> None:
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
        self.data = clear_data


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
    def ask_value(enter, type_, funk_name):
        if enter is None:
            return type_(input(f"Не задано значение {type_.__name__} при вызове метода {funk_name}. "
                               f"Введите значение: "))
        else:
            return enter

class SearchInBook(Book, BackgroundChecks):

    def getter_str_by_index(self, index: int) -> str:
        """
        Метод вызова строки по задаваемому параметру.
        :param index: номер вызываемой строки
        :return: вызываемая строка
        """
        self.is_type(index, int)
        return self.data[index-1]

    def search_num_asked_word(self, question=None) -> print:
        """
        Метод поиска слов по всей книге.
        :param question: искомое слово
        :return: количество совпадений
        """
        question = self.ask_value(question, str, 'search_word')
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

    def divination_by_book(self, question=None) -> print:
        """
        Метод для вызова предложения в задаваемой строке книги.
        :param question: Номер задаваемой строки
        :return: Предложение из задаваемой строки
        """
        question = self.ask_value(question, int, 'divination_by_book')
        self.is_type(question, int)
        counter, sentence = 0, []
        str_ = self.getter_str_by_index(question).split('.')
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
    book.name("Федор Михайлович Достоевский - Преступление и наказание")
    print(book.search_num_asked_word("тварь"))
    print(book.how_many_str())
    print(book.divination_by_book())
