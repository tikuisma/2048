import random

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
        self.pelialusta = []
        for i in range(4):
            self.pelialusta.append([0]*4)

        print("Voit liikkua pelialustalla seuraavilla näppäimillä:")
        print("'W' or 'w' = Ylös")
        print("'S' or 's' = Alas")
        print("'A' or 'a' = Vasemmalle")
        print("'D' or 'd' = Oikealle")

        self.vapaat_paikat = []
        self.siirtojen_lkm = 0

    def ilmestyva_numero(self):
        """Pelin alkaessa pelialustalle tulee satunnaiseen kohtaan joko numero
        2 tai 4 sekä aina siirtojen jälkeen, pelialustalle tulee satunnaiseen
        vapaaseen kohtaan numero 2 tai 4.
        """

        numerot = [2, 4]
        numero = random.choice(numerot)
        self.numeron_asetus(numero)

    def etsi_nollat(self):
        """Etsii pelilaudalta vapaat paikat eli nollien sijainnit.
        """

        self.vapaat_paikat = []
        for i in range(len(self.pelialusta)):
            for j in range(len(self.pelialusta[i])):
                if self.pelialusta[i][j] == 0:
                    self.vapaat_paikat.append((i,j))

    def numeron_asetus(self, numero):
        """Asettaa pelilaudalle numeron 2 tai 4 satunnaisesti. Tarkistaa vapaan
        paikan numeron asettamiselle sekä katsoo myös onko vapaita paikkoja
        jäljellä. Mikäli vapaita paikkoja ei enää ole, peli loppuu.

        Args:
            numero: Pelialustalle arvottu numero.
        """

        self.etsi_nollat()
       # print(self.vapaat_paikat)
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
        self.siirtojen_lkm += 1

        if suunta == "W" or suunta == "w":
            self.kaanto(1)
            self.poista_nollat()
            self.yhdistyminen()
            self.kaanto(3)
        if suunta == "s" or suunta == "S":
            self.kaanto(3)
            self.poista_nollat()
            self.yhdistyminen()
            self.kaanto(1)
        if suunta == "a" or suunta == "A":
            self.poista_nollat()
            self.yhdistyminen()
        if suunta == "d" or suunta == "D":
            self.kaanto(2)
            self.poista_nollat()
            self.yhdistyminen()
            self.kaanto(2)

    def lisaa_nollat(self, ei_nollia):
        """Lisää poistetut nollat takaisin vapaisiin kohtiin pelialustalla,
        jotta pelialusta oli taas "kokonainen".

        Args:
            ei_nollia: Pelialusta, josta puuttuvat vapaat paikat eli nollat.
        """
        print(ei_nollia)
        for i in range(len(ei_nollia)):
            while len(ei_nollia[i]) < 4:
                ei_nollia[i].append(0)
        self.pelialusta = ei_nollia

    def yhdistyminen(self):
        """Siirron jälkeen katsotaan vierekkäiset numerot, jotta ne voitaisiin
        mahdollisesti yhdistää toisiinsa.
        """

        ei_nollia = self.poista_nollat()
        uusi_pelialusta = []
        for i in ei_nollia:
            if len(i) > 1:
                uusi_rivi = []
                j = 0
                while j < len(i):
                    print(j)
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
        self.lisaa_nollat(uusi_pelialusta)

    def poista_nollat(self):
        """Tarkistaa vapaat paikat pelialustalla eli nollien paikat, jonka
        jälkeen poistaa nämä.

        Returns:
            ei_nollia: palauttaa pelialustan, josta on poistettu vapaat paikat.
        """

        ei_nollia = self.pelialusta
        self.etsi_nollat()
        for i in range(len(self.vapaat_paikat)-1,-1,-1):
            ei_nollia[self.vapaat_paikat[i][0]].pop(self.vapaat_paikat[i][1])

        return ei_nollia

    def kaanto(self, kierrokset):
        """Jos käyttäjä on valinnut suunnaksi ylos, alas tai oikealle.
        Käännetään pelialustaa suunnan mukaisesti määrätyllä määrällä, jotta
        voidaan käyttää yhdistyminen-metodia yhdistämään pelialustalla
        yhdistyvät numerot.

        Args:
            kierrokset: Käyttäjän valitseman suunnan mukaan annettu määrä,
            jonka listan tulee kääntyä, jotta numerot saadaan tasattua vasem-
            malle.
        """

        for kierros in range(kierrokset):
            tyhja = [[],[],[],[]]
            for i in range(4):
                for j in range(3, -1, -1):
                    tyhja[j].append(self.pelialusta[i][::-1][j])
            self.pelialusta = tyhja

    def __str__(self) -> str:
        """Tulostaa tekstikäyttöliittymässä näkyvän pelialustan.

        Returns:
            tuloste: palauttaa pelialustan.
        """

        tuloste = f"{self.pelialusta[0]}\n{self.pelialusta[1]}\
        \n{self.pelialusta[2]}\n{self.pelialusta[3]}"

        return tuloste
