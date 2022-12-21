import sys
import copy
from peli import Pelialusta

class Algoritmi:
    """Luokka, joka luo Minimax-algoritmin, jotta peli pelaisi itse itseään.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo pelialustan.

        Args:
            peli: Luo pelin, kutsumalla Pelialusta-luokkaa.
            kokeileva_peli: On ns. kopio pelistä, joka testaa mahdolliset
            vaihtoehdot ja käy ne läpi, jotta algoritmi voi valita parhaimman
            suunnan vaihtoehdoista.
        """

        self.peli = Pelialusta()
        self.kokeileva_peli = Pelialusta()

    def mahdolliset_siirrot(self, pelilauta):
        """Kokeillaan mahdolliset pelilaudan siirtosuunnat ja palautetaan ne
        listana.
        """

        alkuperainen = copy.deepcopy(pelilauta)
        self.kokeileva_peli.pelialusta = copy.deepcopy(pelilauta)
        siirrot = []

        self.kokeileva_peli.siirto("w")
        if alkuperainen != self.kokeileva_peli.pelialusta:
            siirrot.append("w")

        self.kokeileva_peli.pelialusta = copy.deepcopy(pelilauta)
        self.kokeileva_peli.siirto("s")
        if alkuperainen != self.kokeileva_peli.pelialusta:
            siirrot.append("s")

        self.kokeileva_peli.pelialusta = copy.deepcopy(pelilauta)
        self.kokeileva_peli.siirto("a")
        if alkuperainen != self.kokeileva_peli.pelialusta:
            siirrot.append("a")

        self.kokeileva_peli.pelialusta = copy.deepcopy(pelilauta)
        self.kokeileva_peli.siirto("d")
        if alkuperainen != self.kokeileva_peli.pelialusta:
            siirrot.append("d")

        return siirrot

    def pelilaudan_arvo(self, pelilauta):
        """Hyötyfunktio Minmax-algoritmille, joka laskee arvon sen hetkiselle
        pelilaudalle.
        Minimoi erotukset ja pyrkii siirtämään pelilaudalla olevan isoimman
        numeron vasempaan ylänurkkaan sekä maksimoimaan tyhjien ruutujen määrän.
        """

        pelilaudan_painotus = [
        [4**10, 4**9, 4**8, 4**7],
        [4**9, 4**8, 4**7, 4**6],
        [4**8, 4**7, 4**6, 4**5],
        [4**6, 4**5, 4**4, 4**3]
        ]
        painotettu = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.kokeileva_peli.pelialusta = pelilauta
        summa = 0
        for y in range(4):
            for x in range(4):
                tulos = pelilauta[y][x] * pelilaudan_painotus[y][x]
                summa += tulos
                painotettu[y][x] = tulos

        rivi_erotus = 0
        for rivi in painotettu:
            rivi_erotus += (rivi[0] - rivi[1]) * 0.6 + rivi[1] - rivi[2] + rivi[2] - rivi[3]

        sarake_erotus = 0
        for i in range(4):
            sarake_erotus += ((painotettu[0][i] - painotettu[1][i]) * 0.5 + painotettu[1][i]
            -painotettu[2][i] + painotettu[2][i] - painotettu[3][i])

        arvo = summa - (rivi_erotus * 0.5 + sarake_erotus * 0.4)

        self.kokeileva_peli.etsi_nollat(pelilauta)
        arvo = arvo / (16 - len(self.kokeileva_peli.vapaat_paikat))

        return arvo

    def min_siirrot(self, pelilauta):
        """Metodi katsoo ns. vastapelaajan Min:n siirrot.
        """

        self.kokeileva_peli.etsi_nollat(pelilauta)
        siirrot = self.kokeileva_peli.vapaat_paikat
        siirrot2 = []
        for tyhja in siirrot:
            tyhja = list(tyhja)
            tyhja2 = list(tyhja)
            tyhja.append(2)
            siirrot2.append(tyhja)
            tyhja2.append(4)
            siirrot2.append(tyhja2)

        return siirrot2

    def maksimointi(self, pelilauta, alpha, beta, syvyys):
        """Pyrkii löytämään parhaimman suunnan pelilaudalla olevista neljästä
        vaihtoehdosta.
        """

        (maksimisiirto, maksimiarvo) = (None, -1)
        mahdolliset_siirrot = self.mahdolliset_siirrot(pelilauta)

        if syvyys == 0 or len(mahdolliset_siirrot) == 0:
            return (None, self.pelilaudan_arvo(pelilauta))

        syvyys -= 1

        for siirto in mahdolliset_siirrot:
            self.kokeileva_peli.pelialusta = copy.deepcopy(pelilauta)
            self.kokeileva_peli.siirto(siirto)
            (_, arvo) = self.minimointi(self.kokeileva_peli.pelialusta, alpha, beta, syvyys)

            if arvo > maksimiarvo:
                (maksimisiirto, maksimiarvo) = (siirto, arvo)
            if maksimiarvo >= beta:
                break
            if maksimiarvo > alpha:
                alpha = maksimiarvo

        return (maksimisiirto, maksimiarvo)

    def minimointi(self, pelilauta, alpha, beta, syvyys):
        """Pyrkii löytämään ns. vastapelaajan parhaimman siirron eli käytännössä
        mikä on huonoin numero eli 2 tai 4, joka voi pelilaudalle ilmestyä.
        Katsoo kaikki vaihtoehdot pelilaudan vapaista paikoista läpi.
        """

        (minimisiirto, minimiarvo) = (None, sys.maxsize)
        mahdolliset_siirrot = self.min_siirrot(pelilauta)

        if syvyys == 0 or len(mahdolliset_siirrot) == 0:
            return (None, self.pelilaudan_arvo(pelilauta))

        syvyys -= 1

        for siirto in mahdolliset_siirrot:
            pelialusta = copy.deepcopy(pelilauta)
            pelialusta[siirto[0]].pop(siirto[1])
            pelialusta[siirto[0]].insert(siirto[1], siirto[2])

            (_, arvo) = self.maksimointi(pelialusta, alpha, beta, syvyys)

            if arvo < minimiarvo:
                (minimisiirto, minimiarvo) = (siirto, arvo)
            if minimiarvo <= alpha:
                break
            if minimiarvo < beta:
                beta = minimiarvo

        return (minimisiirto, minimiarvo)
