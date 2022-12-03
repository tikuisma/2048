import unittest
from peli import Pelialusta
from algoritmi import Algoritmi

class TestPelialusta(unittest.TestCase):
    def setUp(self):
        self.alusta = Pelialusta()
        self.minmax = Algoritmi()
        self.alusta.pelialusta = [[0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    
    def test_mahdolliset_siirrot(self):
        self.assertEqual(self.minmax.mahdolliset_siirrot(self.alusta.pelialusta), ['s', 'a', 'd'])

        self.alusta.pelialusta = [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(self.minmax.mahdolliset_siirrot(self.alusta.pelialusta), ['s', 'd'])

        self.alusta.pelialusta = [[4, 2, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(self.minmax.mahdolliset_siirrot(self.alusta.pelialusta), ['w', 's', 'd'])

        self.alusta.pelialusta = [[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(self.minmax.mahdolliset_siirrot(self.alusta.pelialusta), ['s', 'a', 'd'])

        self.alusta.pelialusta = [[4, 2, 4, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(self.minmax.mahdolliset_siirrot(self.alusta.pelialusta), ['s'])

        self.alusta.pelialusta = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0]]
        self.assertEqual(self.minmax.mahdolliset_siirrot(self.alusta.pelialusta), ['w', 'a', 'd'])

    def test_pelilaudan_arvo(self):
        self.assertEqual(self.minmax.pelilaudan_arvo(self.alusta.pelialusta), 2)

        self.alusta.pelialusta = [[0, 0, 0, 0], [4, 2, 0, 0], [4, 0, 0, 0], [0, 0, 2, 0]]
        self.assertEqual(self.minmax.pelilaudan_arvo(self.alusta.pelialusta), 3)

    def test_min_siirrot(self):
        self.alusta.pelialusta = [[4, 2, 4, 2], [2, 4, 4, 2], [0, 2, 2, 2], [2, 2, 4, 0]]
        self.assertEqual(self.minmax.min_siirrot(self.alusta.pelialusta), [[2, 0, 2], [2, 0, 4], [3, 3, 2], [3, 3, 4]])
