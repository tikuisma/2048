from peli import Pelialusta
import sys

# HUOM! EI VIELÄ TOIMINNASSA!!

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
    #palauttaa listan mahdollisista siirtosuunnista
        """Kokeillaan mahdolliset pelilaudan siirtosuunnat ja palautetaan ne
        listana
        """

        alkuperainen = str(pelilauta)
        self.kokeileva_peli.pelialusta = pelilauta
        siirrot = []

        self.kokeileva_peli.siirto("w")
        if alkuperainen != self.kokeileva_peli.pelialusta:
            siirrot.append("w")

        self.kokeileva_peli.pelialusta = pelilauta
        self.kokeileva_peli.siirto("s")
        if alkuperainen != self.kokeileva_peli.pelialusta:
            siirrot.append("s")

        self.kokeileva_peli.pelialusta = pelilauta
        self.kokeileva_peli.siirto("a")
        if alkuperainen != self.kokeileva_peli.pelialusta:
            siirrot.append("a")

        self.kokeileva_peli.pelialusta = pelilauta
        self.kokeileva_peli.siirto("d")
        if alkuperainen != self.kokeileva_peli.pelialusta:
            siirrot.append("d")

        return siirrot

    def pelilaudan_arvo(self, pelilauta):
    #laskee pelilaudan arvon eli minkä perusteella siirto tehdään
        self.kokeileva_peli.pelialusta = pelilauta
        summa = 0
        for rivi in pelilauta:
            for numero in rivi:
                summa += numero

        self.kokeileva_peli.etsi_nollat()
        arvo = summa / (16 - len(self.kokeileva_peli.vapaat_paikat))

        return arvo

    def maksimointi(self, pelilauta, a, b, syvyys):
        (maksimisiirto, maksimiarvo) = (None, -1) #pienempi arvo kuin mikään muu
        if self.kokeileva_peli.peli_havitty == True:
            print("Peli on päättynyt")
            #katkaisu ja palautus
        if self.kokeileva_peli.peli_loppu == True:
            print("Peli on päättynyt")
            #katkaisu ja palautus

        for siirto in self.mahdolliset_siirrot(pelilauta):
            self.kokeileva_peli.pelialusta = pelilauta
            self.kokeileva_peli.siirto(siirto)

            #kutsutaan minimointia
            if arvo > maksimiarvo:
                (maksimisiirto, maksimiarvo) = (siirto, arvo)
            if maksimiarvo >= b:
                break
            if maksimiarvo > a:
                a = maksimiarvo

        return (maksimisiirto, maksimiarvo)

    def minimointi(self, pelilauta, a, b, syvyys):
        (minimisiirto, minimiarvo) = (None, sys.maxsize)
        if self.kokeileva_peli.peli_havitty == True:
            print("Peli on päättynyt")
            #katkaisu ja palautus
        if self.kokeileva_peli.peli_loppu == True:
            print("Peli on päättynyt")
            #katkaisu ja palautus

        for siirto in self.mahdolliset_siirrot(pelilauta):
            self.kokeileva_peli.pelialusta = pelilauta
            self.kokeileva_peli.siirto(siirto)

            #kutsutaan minimointia
            if arvo < minimiarvo:
                (minimisiirto, minimiarvo) = (siirto, arvo)
            if minimiarvo <= a:
                break
            if minimiarvo < b:
                b = minimiarvo

        return (minimisiirto, minimiarvo)

    def siirrot():
        pass#min tai max

    def peli_lopussa():
        #
        pass
