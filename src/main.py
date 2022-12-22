import sys
import time
import copy
from datetime import datetime
from peli import Pelialusta
from algoritmi import Algoritmi

def main():
    """Pääfunktio, josta kutsutaan pelialustan tekevää luokkaa ja sen metodeita.
    Args:
        Pelialusta: kutsutaan luokkaa, joka luo pelialustan ja, joka sisältää
        pelin toiminnot.
        Algoritmi: kutsutaan luokkaa, jossa on toteutettuna MinMax-algoritmi
        alpha beta karsinnalla. Luokka laskee parhaimman mahdollisen siirron
        pelissä ja pelaa tätä itse.
    """

    syotteet = ["a","w","d","s"]

    valinta = input("Jos haluat pelata itse, syötä X. Mikäli haluat katsoa,\n"
    "tekoälyn pelaamista, valitse Y.\n"
    "Syötä valintasi: ")

    if valinta.lower() == "x":
        peli = Pelialusta()
        peli.ilmestyva_numero()
        print("Voit liikkua pelialustalla seuraavilla näppäimillä:")
        print("'W' or 'w' = Ylös")
        print("'S' or 's' = Alas")
        print("'A' or 'a' = Vasemmalle")
        print("'D' or 'd' = Oikealle")
        print(peli)
        while peli.peli_havitty is False and peli.peli_loppu is False:
            syote = input("Anna suunta: ")
            if syote.lower() in syotteet:
                ennen = str(peli.pelialusta)
                peli.siirto(syote)
                if ennen != str(peli.pelialusta):
                    peli.ilmestyva_numero()
                    print(peli)
                else:
                    print("Tähän suuntaan ei voi siirtää, kokeile toista suuntaa.")
            else:
                print("Väärä komento")

    if valinta.lower() == "y":
        while True:
            try:
                odotusaika = int(input("Anna odotusaika sekunteina: "))
                pelikierrosten_maara = int(input("Monta kierrosta pelataan? "))
                break
            except:
                print("Virheellinen syöte")
        aloitusaika = datetime.now()
        voitot = 0
        tulokset = []
        for pelikierros in range(int(pelikierrosten_maara)):
            minmax = Algoritmi()
            pelilauta = Pelialusta()
            pelilauta.ilmestyva_numero()
            while not pelilauta.peli_loppu:
                testialusta = copy.copy(pelilauta.pelialusta)
                (siirto, arvo) = minmax.maksimointi(testialusta, -(sys.maxsize * 2), sys.maxsize * 2, 5)
                print("Peli ",pelikierros + 1, ", Siirto: ", siirto, ", Arvo: ", round(arvo))
                if siirto is not None:
                    pelilauta.siirto(siirto)
                    pelilauta.ilmestyva_numero()
                    print(pelilauta)
                    time.sleep(float(odotusaika))
                else:
                    tulokset.append(pelilauta.summa)
                    print("Peli päättyi, ei voittoa!")
                    break
            if pelilauta.peli_loppu:
                print("VOITIT !")
                tulokset.append(pelilauta.summa)
                voitot += 1

    else:
        print("Et valinnut kumpaakaan. Ole hyvä ja yritä uudelleen.")

    lopetusaika = datetime.now()
    print("Voitit: ", voitot, "/", pelikierrosten_maara)
    print("Tulokset: ", tulokset)
    print("Yhteensä aikaa kului: ", lopetusaika - aloitusaika)


if __name__ == "__main__":
    main()
