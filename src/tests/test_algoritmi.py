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

        self.alusta.pelialusta = [[4, 8, 4, 32],[16, 64, 512, 128],[4, 8, 32, 16],[0, 0, 16, 128]]
        self.assertEqual(self.minmax.mahdolliset_siirrot(self.alusta.pelialusta), ['s', 'a'])

    def test_pelilaudan_arvo(self):
        self.assertEqual(self.minmax.pelilaudan_arvo(self.alusta.pelialusta), 314572.8)

        self.alusta.pelialusta = [[0, 0, 0, 0], [4, 2, 0, 0], [4, 0, 0, 0], [0, 0, 2, 0]]
        self.assertEqual(self.minmax.pelilaudan_arvo(self.alusta.pelialusta), 196787.19999999998)

    def test_min_siirrot(self):
        self.alusta.pelialusta = [[4, 2, 4, 2], [2, 4, 4, 2], [0, 2, 2, 2], [2, 2, 4, 0]]
        self.assertEqual(self.minmax.min_siirrot(self.alusta.pelialusta), [[2, 0, 2], [2, 0, 4], [3, 3, 2], [3, 3, 4]])

    def test_minimointi_nolla(self):
        self.alusta.pelialusta = [[4, 2, 8, 2], [4, 4, 2, 4], [8, 2, 4, 2], [4, 16, 8, 4]]
        self.assertEqual(self.minmax.minimointi(self.alusta.pelialusta, -1, sys.maxsize, 0), (None, 253534.4))

    def test_minimointi(self):
        self.alusta.pelialusta = [[4, 2, 8, 2], [2, 4, 2, 4], [8, 2, 4, 0], [0, 16, 8, 4]]
        self.assertEqual(self.minmax.minimointi(self.alusta.pelialusta, -1, sys.maxsize, 2), ([2, 3, 2], 255781.5466666667))

        self.alusta.pelialusta = [[256, 0, 8, 2], [2, 0, 16, 4], [16, 2, 4, 0], [0, 16, 8, 4]]
        self.assertEqual(self.minmax.minimointi(self.alusta.pelialusta, -1, sys.maxsize, 5), ([3, 0, 2], 10570408.36923077))

    def test_maksimointi(self):
        self.alusta.pelialusta = [[4, 2, 8, 2], [2, 4, 2, 4], [8, 2, 4, 2], [2, 16, 8, 4]]
        self.assertEqual(self.minmax.maksimointi(self.alusta.pelialusta, -1, sys.maxsize, 0), (None, 236587.2))

        self.alusta.pelialusta = [[256, 2, 8, 2], [256, 4, 2, 64], [8, 0, 16, 2], [2, 16, 0, 0]]
        self.assertEqual(self.minmax.maksimointi(self.alusta.pelialusta, -1, sys.maxsize, 3), ('a', 24665944.436363637))

        self.alusta.pelialusta = [[0, 2, 0, 2], [2, 0, 0, 0], [0, 0, 4, 0], [0, 0, 0, 0]]
        self.assertEqual(self.minmax.maksimointi(self.alusta.pelialusta, -1, sys.maxsize, 5), ('w', 1130700.8))

        self.alusta.pelialusta = [[8, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2], [4, 0, 4, 2]]
        self.assertEqual(self.minmax.maksimointi(self.alusta.pelialusta, -1, sys.maxsize, 5), ('s', 734003.2))

        self.alusta.pelialusta = [[4, 8, 4, 32],[16, 64, 512, 128],[4, 8, 32, 16],[0, 0, 16, 128]]
        self.assertEqual(self.minmax.maksimointi(self.alusta.pelialusta,-1, sys.maxsize, 2), ('a', 1128436.9066666667))