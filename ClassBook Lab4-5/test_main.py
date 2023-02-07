import unittest
import coverage

from main import BookGames


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.book = BookGames("Ф.М. Достоевский - Преступление и наказание.txt")

    def setUp(self):
        book = BookGames("Ф.М. Достоевский - Преступление и наказание.txt")

    def test_is_type(self):
        with self.assertRaises(TypeError):
            self.book.is_type(2, str)

    def test_in_range(self):
        with self.assertRaises(ValueError):
            self.book.in_range(2, 1)

    def test_ask_value(self):
        self.assertEqual(self.book.ask_value(1, int), 1)

    def test_getter_str(self):
        self.assertEqual(self.book.getter_str(1), "Ф. ДОСТОЕВСКИЙ")
        self.assertEqual(self.book.getter_str(2), "ПРЕСТУПЛЕНИЕ И НАКАЗАНИЕ")

    def test_search_word(self):
        self.assertEqual(self.book.search_word("тварь"), "Слово 'тварь' найдено 12 раз(а).")
        self.assertEqual(self.book.search_word("право"), "Слово 'право' найдено 99 раз(а).")

    def test_how_many_str(self):
        self.assertEqual(self.book.how_many_str(),
                         "В книге Ф.М. Достоевский - Преступление и наказание. - 4115 строк(и).")

    def test_divination_by_book(self):
        self.assertEqual(self.book.divination_by_book(100), "— Я вам проценты еще за месяц внесу; потерпите.")


if __name__ == '__main__':
    unittest.main()

