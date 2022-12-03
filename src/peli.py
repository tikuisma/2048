import random
import copy

class Pelialusta:
    """Luokka, jonka avulla luodaan pelille alusta ja sen toiminnot.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo pelialustan.

        Args:
            peli_havitty: Muuttuja-tieto siitä, että onko peli vielä käynnissä.
            Oletusarvona False eli on käynnissä, mikäli muuttuu True:ksi, peli
            on joko hävitty tai pelattu loppuun saakka.
            pelialusta: Lista, joka on 4x4-kokoinen ja toimii pelialustana.
            vapaat_paikat: Lista, jossa tiedot nollien sijainnista eli pelialus-
            talla olevista vapaista paikoista.
        """

        self.peli_havitty = False
        self.peli_loppu = False
        self.pelialusta = []
        for _ in range(4):
            self.pelialusta.append([0]*4)

        self.vapaat_paikat = []
        self.summa = 0

    def ilmestyva_numero(self):
        """Pelin alkaessa pelialustalle tulee satunnaiseen kohtaan joko numero
        2 tai 4 sekä aina siirtojen jälkeen, pelialustalle tulee satunnaiseen
        vapaaseen kohtaan numero 2 tai 4.
        """

        numerot = [2, 4, 2, 2, 2, 2, 2, 2, 2, 2]
        numero = random.choice(numerot)
        self.numeron_asetus(numero)

    def etsi_nollat(self, pelialusta):
        """Etsii pelilaudalta vapaat paikat eli nollien sijainnit.
        """

        self.vapaat_paikat = []
        for i in range(len(pelialusta)):
            for j in range(len(pelialusta[i])):
                if pelialusta[i][j] == 0:
                    self.vapaat_paikat.append((i,j))

    def numeron_asetus(self, numero):
        """Asettaa pelilaudalle numeron 2 tai 4 satunnaisesti. Tarkistaa vapaan
        paikan numeron asettamiselle sekä katsoo myös onko vapaita paikkoja
        jäljellä. Mikäli vapaita paikkoja ei enää ole, peli loppuu.

        Args:
            numero: Pelialustalle arvottu numero.
        """

        self.etsi_nollat(self.pelialusta)
        if len(self.vapaat_paikat) == 0:
            self.peli_havitty = True
        else:
            paikka = random.choice(self.vapaat_paikat)

            self.pelialusta[paikka[0]].pop(paikka[1])
            self.pelialusta[paikka[0]].insert(paikka[1], numero)

    def siirto(self, suunta):
        """Syötteen mukaan siirrot ylös, alas, vasemmalle tai oikealle.
        Käyttäjän antaman syötteen mukaan tehtävät siirrot pelialustalla.

        Args:
            suunta: Käyttäjän antama syöte halutusta suunnasta pelialustalla.
        """
        if suunta in ["W", "w"]:
            pelialusta = self.kaanto(1, self.pelialusta)
            pelialusta = self.poista_nollat(pelialusta)
            pelialusta = self.yhdistyminen(pelialusta)
            pelialusta = self.lisaa_nollat(pelialusta)
            self.pelialusta = self.kaanto(3, pelialusta)
        if suunta in ["s", "S"]:
            pelialusta = self.kaanto(3, self.pelialusta)
            pelialusta = self.poista_nollat(pelialusta)
            pelialusta = self.yhdistyminen(pelialusta)
            pelialusta = self.lisaa_nollat(pelialusta)
            self.pelialusta = self.kaanto(1, pelialusta)
        if suunta in ["a", "A"]:
            pelialusta = self.poista_nollat(self.pelialusta)
            pelialusta = self.yhdistyminen(pelialusta)
            self.pelialusta = self.lisaa_nollat(pelialusta)
        if suunta in ["d", "D"]:
            pelialusta = self.kaanto(2, self.pelialusta)
            pelialusta = self.poista_nollat(pelialusta)
            pelialusta = self.yhdistyminen(pelialusta)
            pelialusta = self.lisaa_nollat(pelialusta)
            self.pelialusta = self.kaanto(2, pelialusta)

        self.peli_voitettu()

    def lisaa_nollat(self, ei_nollia):
        """Lisää poistetut nollat takaisin vapaisiin kohtiin pelialustalla,
        jotta pelialusta oli taas "kokonainen".

        Args:
            ei_nollia: Pelialusta, josta puuttuvat vapaat paikat eli nollat.
        """

        for i in range(len(ei_nollia)):
            while len(ei_nollia[i]) < 4:
                ei_nollia[i].append(0)

        return ei_nollia

    def yhdistyminen(self, pelialusta):
        """Siirron jälkeen katsotaan vierekkäiset numerot, jotta ne voitaisiin
        mahdollisesti yhdistää toisiinsa.
        """

        ei_nollia = self.poista_nollat(pelialusta)
        uusi_pelialusta = []
        for i in ei_nollia:
            if len(i) > 1:
                uusi_rivi = []
                j = 0
                while j < len(i):
                    if j == len(i)-1:
                        uusi_luku = i[j]
                        j += 1
                    elif i[j] == i[j+1]:
                        uusi_luku = i[j] + i[j+1]
                        j += 2
                        ei_sama = False
                    else:
                        uusi_luku = i[j]
                        j += 1
                        ei_sama = True
                    uusi_rivi.append(uusi_luku)
                    if ei_sama and j == len(i)-1:
                        uusi_luku = i[j]
                        uusi_rivi.append(uusi_luku)
                        j += 1
                uusi_pelialusta.append(uusi_rivi)
            else:
                uusi_pelialusta.append(i)

        return uusi_pelialusta

    def poista_nollat(self, pelialusta):
        """Tarkistaa vapaat paikat pelialustalla eli nollien paikat, jonka
        jälkeen poistaa nämä.

        Returns:
            ei_nollia: palauttaa pelialustan, josta on poistettu vapaat paikat.
        """

        ei_nollia = pelialusta
        self.etsi_nollat(ei_nollia)
        for i in range(len(self.vapaat_paikat)-1,-1,-1):
            ei_nollia[self.vapaat_paikat[i][0]].pop(self.vapaat_paikat[i][1])

        return ei_nollia

    def kaanto(self, kierrokset, pelialusta):
        """Jos käyttäjä on valinnut suunnaksi ylos, alas tai oikealle.
        Käännetään pelialustaa suunnan mukaisesti määrätyllä määrällä, jotta
        voidaan käyttää yhdistyminen-metodia yhdistämään pelialustalla
        yhdistyvät numerot.

        Args:
            kierrokset: Käyttäjän valitseman suunnan mukaan annettu määrä,
            jonka listan tulee kääntyä, jotta numerot saadaan tasattua vasem-
            malle.
        """
        uusi_pelialusta = copy.deepcopy(pelialusta)

        for _ in range(kierrokset):
            tyhja = [[],[],[],[]]
            for i in range(4):
                for j in range(3, -1, -1):
                    tyhja[j].append(uusi_pelialusta[i][::-1][j])
            uusi_pelialusta = tyhja

        return uusi_pelialusta

    def peli_voitettu(self):
        max_arvo = 2048
        self.summa = 0
        for i in self.pelialusta:
            if max(i) == max_arvo:
                self.peli_loppu = True
            for j in i:
                self.summa += j


    def __str__(self) -> str:
        """Tulostaa tekstikäyttöliittymässä näkyvän pelialustan.

        Returns:
            tuloste: palauttaa pelialustan.
        """

        tuloste = f"{self.pelialusta[0]}\n{self.pelialusta[1]}\
        \n{self.pelialusta[2]}\n{self.pelialusta[3]}"

        return tuloste
