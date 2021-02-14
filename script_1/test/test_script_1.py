import unittest
from script_1 import GetAuthorsAndBooks

class Script1Test(unittest.TestCase):

    def setUp(self):
        self.init_author_andbooks = GetAuthorsAndBooks(
        )

    def test_all_authors_names_and_books_num(self):
        self.assertEqual(
            self.init_author_andbooks.get_values(),
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