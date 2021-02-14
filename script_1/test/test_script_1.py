import unittest
from script_1 import GetAuthorsAndBooks

class Script1Test(unittest.TestCase):

    def setUp(self):
        self.init_author_andbooks = GetAuthorsAndBooks(
        )

    def test_all_authors_names_and_books_num(self):
        self.assertEqual(
            self.init_author_andbooks.fetch_data(),
            [
                {"name": "Christy Batz", "book_count": 0},
                {"name": "Dr. Shyann Abbott DVM", "book_count": 1},
                {"name": "Noelia Kling", "book_count": 0},
                {"name": "Dr. Gabriel Schmitt Jr.", "book_count": 1},
                {"name": "Dr. Federico Thiel", "book_count": 1},
                {"name": "Lolita Jakubowski", "book_count": 3},
                {"name": "Dr. Deondre Cassin DVM", "book_count": 1},
                {"name": "Catalina Rowe", "book_count": 0},
                {"name": "Asha Nader III", "book_count": 0},
                {"name": "Prof. Ova Hayes I", "book_count": 1},
            ]
        )

class Excercise3Test(unittest.TestCase):

    def setUp(self):
        self.init_get_author = GetAuthorsAndBooks()

    def test_author_1(self):
        self.assertEqual(
            self.init_get_author.fetch_data(1),
            {"name": "Christy Batz", "book_count": 0}
        )
    def test_author_2(self):
        self.assertEqual(
            self.init_get_author.fetch_data(2),
            {"name": "Dr. Shyann Abbott DVM", "book_count": 1}
        )
    def test_author_3(self):
        self.assertEqual(
            self.init_get_author.fetch_data(3),
            {"name": "Noelia Kling", "book_count": 0}
        )
    def test_author_4(self):
        self.assertEqual(
            self.init_get_author.fetch_data(4),
            {"name": "Dr. Gabriel Schmitt Jr.", "book_count": 1},
        )
    def test_author_5(self):
        self.assertEqual(
            self.init_get_author.fetch_data(5),
            {"name": "Dr. Federico Thiel", "book_count": 1}
        )
    def test_author_6(self):
        self.assertEqual(
            self.init_get_author.fetch_data(6),
            {"name": "Lolita Jakubowski", "book_count": 3}
        )
    def test_author_7(self):
        self.assertEqual(
            self.init_get_author.fetch_data(7),
            {"name": "Dr. Deondre Cassin DVM", "book_count": 1}
        )  
    def test_author_8(self):
        self.assertEqual(
            self.init_get_author.fetch_data(8),
            {"name": "Catalina Rowe", "book_count": 0}
        ) 
    def test_author_9(self):
        self.assertEqual(
            self.init_get_author.fetch_data(9),
            {"name": "Asha Nader III", "book_count": 0}
        ) 
    def test_author_10(self):
        self.assertEqual(
            self.init_get_author.fetch_data(10),
            {"name": "Prof. Ova Hayes I", "book_count": 1}
        )
                                                