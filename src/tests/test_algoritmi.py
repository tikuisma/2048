import unittest
import sys
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

    def test_minimointi_nolla(self):
        self.alusta.pelialusta = [[4, 2, 8, 2], [4, 4, 2, 4], [8, 2, 4, 2], [4, 16, 8, 4]]
        self.assertEqual(self.minmax.minimointi(self.alusta.pelialusta, -1, sys.maxsize, 0), (None, 4.875))

    def test_minimointi(self):
        self.alusta.pelialusta = [[4, 2, 8, 2], [2, 4, 2, 4], [8, 2, 4, 0], [0, 16, 8, 4]]
        self.assertEqual(self.minmax.minimointi(self.alusta.pelialusta, -1, sys.maxsize, 2), ([[4, 2, 8, 2], [2, 4, 2, 4], [8, 2, 4, 2], [0, 16, 8, 4]], 4.8))

        self.alusta.pelialusta = [[256, 0, 8, 2], [2, 0, 16, 4], [16, 2, 4, 0], [0, 16, 8, 4]]
        self.assertEqual(self.minmax.minimointi(self.alusta.pelialusta, -1, sys.maxsize, 5), ([[256, 0, 8, 2], [2, 0, 16, 4], [16, 2, 4, 2], [0, 16, 8, 4]], 26.615384615384617))

    def test_maksimointi(self):
        self.alusta.pelialusta = [[4, 2, 8, 2], [2, 4, 2, 4], [8, 2, 4, 2], [2, 16, 8, 4]]
        self.assertEqual(self.minmax.maksimointi(self.alusta.pelialusta, -1, sys.maxsize, 0), (None, 4.625))

        self.alusta.pelialusta = [[256, 2, 8, 2], [256, 4, 2, 64], [8, 0, 16, 2], [2, 16, 0, 0]]
        self.assertEqual(self.minmax.maksimointi(self.alusta.pelialusta, -1, sys.maxsize, 3), ('a', 58.18181818181818))

        self.alusta.pelialusta = [[0, 2, 0, 2], [2, 0, 0, 0], [0, 0, 4, 0], [0, 0, 0, 0]]
        self.assertEqual(self.minmax.maksimointi(self.alusta.pelialusta, -1, sys.maxsize, 5), ('w', 3.5))

        self.alusta.pelialusta = [[8, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2], [4, 0, 4, 2]]
        self.assertEqual(self.minmax.maksimointi(self.alusta.pelialusta, -1, sys.maxsize, 5), ('s', 6))
