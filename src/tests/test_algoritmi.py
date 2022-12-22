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


    def test_min_siirrot(self):
        self.alusta.pelialusta = [[4, 2, 4, 2], [2, 4, 4, 2], [0, 2, 2, 2], [2, 2, 4, 0]]
        self.assertEqual(self.minmax.min_siirrot(self.alusta.pelialusta), [[2, 0, 2], [2, 0, 4], [3, 3, 2], [3, 3, 4]])


    def test_minimointi_nolla(self):
        self.alusta.pelialusta = [[4, 2, 8, 2], [4, 4, 2, 4], [8, 2, 4, 2], [4, 16, 8, 4]]
        self.assertEqual(self.minmax.minimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 0), (None, 253534.4))


    def test_minimointi(self):
        self.alusta.pelialusta = [
        [4, 2, 8, 2],
        [2, 4, 2, 4],
        [8, 2, 4, 0],
        [0, 16, 8, 4]
        ]
        (siirto1, _) = self.minmax.minimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 4)
        self.assertEqual(siirto1, ([3, 0, 2]))

        self.alusta.pelialusta = [
        [4, 0, 8, 2],
        [2, 0, 16, 4],
        [16, 2, 4, 0],
        [8, 16, 8, 4]
        ]
        (siirto2, _) = self.minmax.minimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 4)
        self.assertEqual(siirto2, ([2, 3, 2]))

        self.alusta.pelialusta = [
        [16, 4, 8, 2],
        [4, 0, 4, 16],
        [16, 4, 4, 2],
        [8, 16, 8, 4]
        ]
        (siirto3, _) = self.minmax.minimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 4)
        self.assertEqual(siirto3, ([1, 1, 2]))

        self.alusta.pelialusta = [
        [2, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
        ]
        (siirto4, _) = self.minmax.minimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 4)
        self.assertEqual(siirto4, ([1, 1, 4]))

        self.alusta.pelialusta = [
        [1024, 0, 1024, 4],
        [4, 32, 4, 16],
        [128, 64, 2, 2],
        [2, 256, 0, 0]
        ]
        (siirto5, _) = self.minmax.minimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 4)
        self.assertEqual(siirto5, ([0, 1, 2]))

        self.alusta.pelialusta = [
        [0, 512, 0, 0],
        [0, 1024, 0, 8],
        [8, 8, 1024, 4],
        [512, 16, 16, 4]
        ]
        (siirto6, _) = self.minmax.minimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 4)
        self.assertEqual(siirto6, ([0, 0, 2]))


    def test_maksimointi(self):
        self.alusta.pelialusta = [
        [512, 2, 8, 4],
        [4, 32, 4, 2],
        [128, 64, 8, 16],
        [2, 256, 2, 2]
        ]
        (siirto, _) = self.minmax.maksimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 5)
        self.assertEqual(siirto, 'a')

        #uusi pelicase

        self.alusta.pelialusta = [
        [1024, 512, 512, 4],
        [4, 32, 4, 2],
        [128, 64, 8, 16],
        [2, 256, 2, 2]
        ]
        (siirto1, _) = self.minmax.maksimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 5)
        self.assertEqual(siirto1, 'a')

        self.alusta.pelialusta = [
        [1024, 1024, 4, 2],
        [4, 32, 4, 2],
        [128, 64, 8, 16],
        [2, 256, 4, 0]
        ]

        (siirto2, _) = self.minmax.maksimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 5)
        self.assertEqual(siirto2, 'w')
        self.alusta.pelialusta = [
        [1024, 1024, 8, 4],
        [4, 32, 8, 16],
        [128, 64, 4, 2],
        [2, 256, 0, 0]
        ]


        (siirto3, _) = self.minmax.maksimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 5)
        self.assertEqual(siirto3, 'w')
        self.alusta.pelialusta = [
        [1024, 1024, 16, 4],
        [4, 32, 4, 16],
        [128, 64, 2, 2],
        [2, 256, 0, 0]
        ]

        (siirto4, _) = self.minmax.maksimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 5)
        self.assertEqual(siirto4, 's')
        self.alusta.pelialusta = [
        [1024, 1024, 0, 2],
        [4, 32, 16, 4],
        [128, 64, 4, 16],
        [2, 256, 2, 2]
        ]

        (siirto5, _) = self.minmax.maksimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 5)
        self.assertEqual(siirto5, 'w')
        self.alusta.pelialusta = [
        [1024, 1024, 16, 2],
        [4, 32, 4, 4],
        [128, 64, 2, 16],
        [2, 256, 4, 2]
        ]

        (siirto6, _) = self.minmax.maksimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 5)
        self.assertEqual(siirto6, 'a')

        #uusi pelicase

        self.alusta.pelialusta = [
        [0, 512, 1024, 8],
        [8, 1024, 16, 2],
        [0, 8, 0, 2],
        [512, 16, 0, 4]
        ]

        (siirto1, _) = self.minmax.maksimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 5)
        self.assertEqual(siirto1, 's')
        self.alusta.pelialusta = [
        [0, 512, 0, 0],
        [0, 1024, 2, 8],
        [8, 8, 1024, 4],
        [512, 16, 16, 4]
        ]

        (siirto2, _) = self.minmax.maksimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 5)
        self.assertEqual(siirto2, 'w')
        self.alusta.pelialusta = [
        [8, 512, 2, 8],
        [512, 1024, 1024, 8],
        [2, 8, 16, 0],
        [0, 16, 0, 0]
        ]

        (siirto3, _) = self.minmax.maksimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 5)
        self.assertEqual(siirto2, 'w')
        self.alusta.pelialusta = [
        [8, 512, 2, 16],
        [512, 1024, 1024, 0],
        [2, 8, 16, 0],
        [0, 16, 0, 0]
        ]

        (siirto4, _) = self.minmax.maksimointi(self.alusta.pelialusta, -(sys.maxsize * 2), sys.maxsize*2, 5)
        self.assertEqual(siirto4, 'a')