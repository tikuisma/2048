from peli import Pelialusta
import algoritmi

def main():
    """Pääfunktio, josta kutsutaan pelialustan tekevää luokkaa ja sen metodeita.
    Args:
        Pelialusta: kutsutaan luokkaa, joka luo pelialustan ja, joka sisältää
        pelin toiminnot.
    """

    syotteet = ["a","A","w","W","d","D","s","S"]

    valinta = input("Jos haluat pelata itse, syötä X. Mikäli haluat katsoa,\n"
    "tekoälyn pelaamista, valitse Y.\n"
    "Syötä valintasi: ")
    if valinta == "X" or valinta == "x":
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
            if syote in syotteet:
                ennen = str(peli.pelialusta)
                peli.siirto(syote)
                if ennen != str(peli.pelialusta):
                    peli.ilmestyva_numero()
                    print(peli)
                else:
                    print("Tähän suuntaan ei voi siirtää, kokeile toista suuntaa.")
            else:
                print("Väärä komento")
    if valinta == "Y" or valinta == "y":
        algoritmi
    else:
        print("Et valinnut kumpaakaan. Ole hyvä ja yritä uudelleen.")

if __name__ == "__main__":
    main()
