import re


class Book:
    def __init__(self, file):
        self.file = file
        self.data = []
        self.loader()
        self.cleaner()

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
            str_ = str_.strip('\n')
            clear_data.append(str_)
        self.data = clear_data


class BackgroundChecks:

    @staticmethod
    def is_type(enter, type_):
        if not isinstance(enter, type_):
            raise TypeError(f"Введённое значение {enter} - не типа {type_}.")


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
        return self.data[index-1]

    def search_word(self, question=None) -> print:
        """
        Метод поиска слов по всей книге.
        :param question: искомое слово
        :return: количество совпадений
        """
        if question is None:
            print("Вы не задали слово. Введите слово количество совпадений которого будем искать:")
            question = str(input())
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
        if question is None:
            print(self.how_many_str())
            print(f"Вы не задали номер строки. Выберите номер строки по которому будете гадать:")
            question = int(input())
            self.is_type(question, int)
        counter, sentence = 0, []
        str_ = self.getter_str(question).split('.')
        for text in str_:
            if text:
                counter += 1
            sentence.append(text)
        if counter == 1:
            return sentence[0] + '.'
        print(f'В указанной строчке {counter} предложения(ий). Введите № предложения от 1 до {counter}:')
        index = int(input())
        if index not in range(1, counter+1):
            raise ValueError(f"Выбранное значение не в пределах от 1 до {counter}")
        return sentence[index-1] + "."


if __name__ == "__main__":
    book = BookGames("Ф.М. Достоевский - Преступление и наказание.txt")
    print(book.getter_str(1), book.getter_str(2), sep=' - ')
    print(book.search_word("право"))
    print(book.divination_by_book(3555))
