from peli import Pelialusta

def main():
    """Pääfunktio, josta kutsutaan pelialustan tekevää luokkaa ja sen metodeita.
    Args:
        Pelialusta: kutsutaan luokkaa, joka luo pelialustan ja, joka sisältää
        pelin toiminnot.
    """

    syotteet = ["a","A","w","W","d","D","s","S"]

    peli = Pelialusta()
    peli.ilmestyva_numero()
    print(peli)
    while peli.peli_havitty is False:
        syote = input("Anna suunta: ")
        if syote in syotteet:
            ennen = str(peli.pelialusta)
            peli.siirto(syote)
            if ennen != str(peli.pelialusta):
                peli.ilmestyva_numero()
            print(peli)
            if peli.siirto(syote) is False:
                print("Väärä komento")
        else:
            print("Väärä komento")

if __name__ == "__main__":
    main()
