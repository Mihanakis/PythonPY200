import unittest
from main import Book


class Test(unittest.TestCase, Book):
    book = Book("Book.txt")

    def test_getter_str(self):
        super(book).getter_str()
        self.assertEqual(getter_str(3), '��� ���������� �������.')

#��� ���������� �������. ����� '����' ������� 103 ���(�).
