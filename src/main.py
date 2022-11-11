from peli import Pelialusta

def main():
    peli = Pelialusta()
    while peli.peli_havitty == False:
        peli.ilmestyva_numero()
        print(peli)
        syote = input("Anna suunta: ")
        if syote == "a" or "A":
            peli.siirto(syote)
  

if __name__ == "__main__":
    main()