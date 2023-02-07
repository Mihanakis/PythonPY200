import re, unittest


class Book:
    """
    Класс для гадания по строчке из книги. Умеет считать количество символов, убирать лишние.
    Снабжена поиском по количеству слов. Перед вводом параметров показывает общее количество строк.
    """
    def __init__(self, file):
        self.file = file
        print(f"Инициализирую экземпляр книги: {self.file}")
        self.data = []
        self.data = self.loader()
        self.data = self.cleaner()

    def __str__(self):
        return self.file.strip('txt')

    def loader(self) -> list:
        """
        Метод построчной загрузки файла книги формата txt в массив.
        :return: массив формата list со строками книги
        """
        print("Вызываю метод loader, создаю массив из txt файла.")
        with open(self.file, "r", encoding='cp1251') as f:
            for word in f:
                self.data.append(word)
        return self.data

    def cleaner(self) -> list:
        """
        Метод очистки строк книги от лишних символов
        :return: массив файла со строками книги
        """
        print("Вызываю метод cleaner, убираю ненужные символы.")
        clear_data = []
        for word in self.data:
            if word not in ['\n']:
                word = word.strip('\n')
                clear_data.append(word)
        self.data = clear_data
        return self.data

    def getter_str(self, question: int) -> str:
        """
        Метод вызова строки по задаваемому параметру.
        :param question: номер вызываемой строки
        :return: вызываемая строка
        """
        print(f"Вызываю метод getter_str для строки №{question}:")
        return self.data[question]

    def counter_word(self, question: str) -> print:
        """
        Метод поиска слов по всей книге.
        :param question: искомое слово
        :return: количество совпадений
        """
        print(f"Выполняю метод класса counter_word, ищу слова '{question}'.")
        question = question.lower()
        counter = 0
        for str_ in self.data:
            word_list = str_.split()
            for word in word_list:
                word = word.lower()
                result = re.match(f'{question}', word)
                if result:
                    counter += 1
        return print(f"Слово '{question}' найдено {counter} раз(а).")

    def how_many_str(self) -> print:
        """
        Метод для подсчёта количества строк в книге.
        :return: количество строк в книге
        """
        print(f"Вызываю метод how_many_str для поиска всех строк в книге {book}:")
        return print(f"В книге {book} - {len(self.data)} строк(и).")

    def divination(self, question=None) -> print:
        """
        Метод для вызова предложения в задаваемой строке книги.
        :param question: Номер задаваемой строки
        :return: Предложение из задаваемой строки
        """
        print(f'Вызываю метод гадания по книге {book}, выбрана строка {question}.')
        if question is None:
            print(f"Вы не задали номер строки. Выберите номер строки по которому будете гадать:")
            question = int(input())
        counter, sentence = 0, []
        str_ = self.getter_str(question).split('.')
        for text in str_:
            if text:
                counter += 1
                sentence.append(text)
        if len(sentence) == 1:
            return print(sentence[0] + '.')
        print(f'В указанной строчке {counter} предложения(ий). Введите № предложения от 1 до {counter}:')
        index = int(input())
        if index not in range(1, counter+1):
            raise ValueError(f"Выбранное значение не в пределах от 1 до {counter}")
        return print(sentence[index-1] + ".")


if __name__ == "__main__":
    book = Book("Book.txt")
    book.counter_word("есть")
    book.divination(4)
    unittest.main()
