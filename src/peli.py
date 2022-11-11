import random

class Pelialusta:
    def __init__(self):
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

    def ilmestyva_numero(self):
        numerot = [2, 4]
        numero = random.choice(numerot)
        self.numeron_asetus(numero)

    def etsi_nollat(self):
        """Etsii pelilaudalta vapaat paikat eli nollat."""
        self.vapaat_paikat = []
        for i in range(len(self.pelialusta)):
            for j in range(len(self.pelialusta[i])):
                if self.pelialusta[i][j] == 0:
                    self.vapaat_paikat.append((i,j))

    def numeron_asetus(self, numero):
        """Asettaa pelilaudalle numeron 2 tai 4 satunnaisesti. Tarkistaa vapaan
        paikan numeron asettamiselle sekä katsoo myös onko vapaita paikkoja
        jäljellä. Mikäli vapaita paikkoja ei enää ole, peli loppuu."""
        self.etsi_nollat()
        print(self.vapaat_paikat)
        if len(self.vapaat_paikat) == 0:
            self.peli_havitty = True
        else:
            paikka = random.choice(self.vapaat_paikat)

            self.pelialusta[paikka[0]].pop(paikka[1])
            self.pelialusta[paikka[0]].insert(paikka[1], numero)
    
    def siirto(self, suunta):
        """Syötteen mukaan siirrot ylös, alas, vasemmalle tai oikealle. (Tällä
        hetkellä siirrot toimivat vasta ainoastaan vasemmalle.)"""
        if suunta == "W" or "w":
            pass
        if suunta == "s" or "S":
            pass
        if suunta == "a":
            self.poista_nollat()
            self.yhdistyminen()
        if suunta == "d" or "D":
            pass
    

    def lisaa_nollat(self, ei_nollia):
        """Lisää poistetut nollat takaisin vapaisiin kohtiin."""
        for i in range(len(ei_nollia)):
            while len(ei_nollia[i]) < 4:
                ei_nollia[i].append(0)
        self.pelialusta = ei_nollia


    def yhdistyminen(self):
        """Katsoo siirron jälkeen vierekkäiset numerot (tällä hetkellä vain
        vasemmalta luettuna) voisiko ne yhdistää toisiinsa."""
        ei_nollia = self.poista_nollat()
        uusi_pelialusta = []
        for i in ei_nollia:
            if len(i) > 1:
                uusi_rivi = []
                j = 0
                while j < len(i)-1:
                    if i[j] == i[j+1]:
                        uusi_luku = i[j] + i[j+1]
                        j += 2
                        ei_sama = False
                        print("sama")
                        print(uusi_luku)

                    else:
                        uusi_luku = i[j]
                        j += 1
                        ei_sama = True
                        print("ei sama")
                    uusi_rivi.append(uusi_luku)
                    if ei_sama and j == len(i)-1:
                        uusi_luku = i[j]
                        uusi_rivi.append(uusi_luku)
                uusi_pelialusta.append(uusi_rivi)
            else:
                uusi_pelialusta.append(i)
        self.lisaa_nollat(uusi_pelialusta)


    def poista_nollat(self):
        """Katsoo missä vapaat paikat eli nollat ovat ja poistaa nämä."""
        ei_nollia = self.pelialusta
        self.etsi_nollat()
        for i in range(len(self.vapaat_paikat)-1,-1,-1):
            ei_nollia[self.vapaat_paikat[i][0]].pop(self.vapaat_paikat[i][1])
 
        return ei_nollia

    #def kaanto(self,kierrokset):
      #  kaannetty = []
       # for 
    #def onko_tilaa(self, vapaat_paikat):

    

    def __str__(self) -> str:
        return str(self.pelialusta)

