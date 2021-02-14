import unittest
from script_2 import GetPages


class Script2Test(unittest.TestCase):

    def setUp(self):
        self.init_get_pages = GetPages()

    def test_all_authors_names_and_books_num(self):
        self.assertEqual(
            self.init_get_pages.get_values(),
            [
                [
                    { "name": "Christy Batz" , "page": 1},
                    { "name": "Dr. Shyann Abbott DVM" , "page": 1},
                    { "name": "Noelia Kling" , "page": 1},
                    { "name": "Dr. Gabriel Schmitt Jr." , "page": 1},
                    { "name": "Dr. Federico Thiel" , "page": 1},
                    { "name": "Lolita Jakubowski" , "page": 1},
                    { "name": "Dr. Deondre Cassin DVM" , "page": 1},
                    { "name": "Catalina Rowe" , "page": 1},
                    { "name": "Asha Nader III" , "page": 1},
                    { "name": "Prof. Ova Hayes I" , "page": 1},
                ],
                [
                    { "name": "Keshaun Emard" , "page": 2},
                    { "name": "Marisa Treutel" , "page": 2},
                    { "name": "Mrs. Krista Huel Jr." , "page": 2},
                    { "name": "Alanis Kuhlman" , "page": 2},
                    { "name": "Clemmie Wuckert" , "page": 2},
                    { "name": "Prof. Gerson Bode II" , "page": 2},
                    { "name": "Elvis Wisozk I" , "page": 2},
                    { "name": "Lydia Schmeler" , "page": 2},
                    { "name": "Rosie Moen" , "page": 2},
                    { "name": "Erika Muller II" , "page": 2},
                ],
                [
                    { "name": "Taya Grady" , "page": 3},
                    { "name": "Zola Bailey" , "page": 3},
                    { "name": "Dr. Cornelius Koelpin II" , "page": 3},
                    { "name": "Alena Jacobi" , "page": 3},
                    { "name": "Columbus Rosenbaum" , "page": 3},
                    { "name": "Sylvia Koepp" , "page": 3},
                    { "name": "Sienna Anderson PhD" , "page": 3},
                    { "name": "Rosetta Cummings" , "page": 3},
                    { "name": "Savanah Gutkowski Jr." , "page": 3},
                    { "name": "Donnell Greenfelder" , "page": 3},
                ],
                [
                    { "name": "Genesis Barrows" , "page": 4},
                    { "name": "Eloy Larson" , "page": 4},
                    { "name": "Emie Dickens" , "page": 4},
                    { "name": "Derek Bergnaum PhD" , "page": 4},
                    { "name": "Prof. Candace Schaden" , "page": 4},
                    { "name": "Hildegard Schuster III" , "page": 4},
                    { "name": "Mrs. Caleigh Windler" , "page": 4},
                    { "name": "Ms. Stefanie Pfeffer" , "page": 4},
                    { "name": "Prof. Eugenia Schroeder V" , "page": 4},
                    { "name": "Brycen Sipes" , "page": 4},
                ],
                [
                    { "name": "Liliane Smitham" , "page": 5},
                    { "name": "Dr. Osborne Cole" , "page": 5},
                    { "name": "Miss Mollie Connelly DDS" , "page": 5},
                    { "name": "Reymundo Nikolaus" , "page": 5},
                    { "name": "Carolanne Sanford" , "page": 5},
                    { "name": "Gunnar Ward" , "page": 5},
                    { "name": "Miss Malika Metz V" , "page": 5},
                    { "name": "Brendon Abshire V" , "page": 5},
                    { "name": "Aylin Gutkowski" , "page": 5},
                    { "name": "Dr. Maverick Fahey II" , "page": 5},
                ]
            ]
        )
