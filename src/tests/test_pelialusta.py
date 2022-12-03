import unittest
from peli import Pelialusta

class TestPelialusta(unittest.TestCase):
    def setUp(self):
        self.alusta = Pelialusta()
        self.alusta.pelialusta = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def test_peli(self):
        self.assertEqual(self.alusta.peli_havitty, False)
        self.assertEqual(self.alusta.vapaat_paikat, [])
        self.assertEqual(self.alusta.pelialusta, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) 

    def test_ilmestyva_numero(self):
        self.alusta.numeron_asetus(2)
        self.assertEqual(len(self.alusta.pelialusta), 4)
        summa = 0
        for i in range(0, 4):
            for x in self.alusta.pelialusta[i]:
                summa += x
        self.assertEqual(summa, 2)

    def test_etsi_nollat_tyhja(self):
        self.alusta.etsi_nollat(self.alusta.pelialusta)
        self.assertEqual(self.alusta.vapaat_paikat, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)])

    def test_etsi_nollat_ei_tyhja(self):
        self.alusta.ilmestyva_numero()
        self.alusta.etsi_nollat(self.alusta.pelialusta)
        self.assertEqual(len(self.alusta.vapaat_paikat), 15)

    def test_peli_havitty(self):
        self.alusta.pelialusta = []
        for i in range(4):
            self.alusta.pelialusta.append([2]*4)
        self.alusta.numeron_asetus(2)
        self.assertEqual(self.alusta.peli_havitty, True)

    def test_lisaa_nollat(self):
        muuttuja = [[4, 2], [], [], []]
        self.assertEqual(self.alusta.lisaa_nollat(muuttuja), [[4, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_poista_nollat(self):
        self.alusta.pelialusta = [[4, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(self.alusta.poista_nollat(self.alusta.pelialusta), [[4, 2], [2], [], []])

    def test_siirto(self):
        self.alusta.pelialusta = [[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.alusta.siirto("W")
        self.assertAlmostEqual(self.alusta.pelialusta, [[0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

        self.alusta.pelialusta = [[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.alusta.siirto("s")
        self.assertAlmostEqual(self.alusta.pelialusta, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0]])

        self.alusta.pelialusta = [[0, 4, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.alusta.siirto("a")
        self.assertAlmostEqual(self.alusta.pelialusta, [[4, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

        self.alusta.pelialusta = [[0, 4, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.alusta.siirto("D")
        self.assertAlmostEqual(self.alusta.pelialusta, [[0, 0, 0, 4], [0, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_str(self):
        self.assertEqual(str(self.alusta), f"{self.alusta.pelialusta[0]}\n{self.alusta.pelialusta[1]}\
        \n{self.alusta.pelialusta[2]}\n{self.alusta.pelialusta[3]}")

    def test_yhdistyminen(self):
        self.alusta.pelialusta = [[0, 0, 0, 0], [2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(self.alusta.yhdistyminen(self.alusta.pelialusta), [[], [4], [], []])

        self.alusta.pelialusta = [[0, 0, 0, 0], [2, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(self.alusta.yhdistyminen(self.alusta.pelialusta), [[], [4, 2], [], []])

        self.alusta.pelialusta = [[0, 0, 0, 0], [2, 4, 2, 4], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(self.alusta.yhdistyminen(self.alusta.pelialusta), [[], [2, 4, 2, 4], [], []])