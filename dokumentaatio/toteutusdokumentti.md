# Toteutusdokumentti

## Ohjelman yleisrakenne
Kooditiedostot on jaettu seuraavanlaisesti:
- src
    - algoritmi.py
    - main.py
    - peli.py
    - tests
        - test_algoritmi.py
        - test_main.py
        - test_pelialusta.py

### Kooditiedostojen sisältö
main.py: Tiedosto toimii pelin käynnistystiedostona. Riippuen pelin pelaaja valinnasta, täältä kutsutaan ``Pelialusta``- ja ``Algoritmi``-luokkaa, jossa on pelin toimintoja.

peli.py: Tiedosto toimii pelin alustana sekä se sisältää pelin toiminnallisuuden. Pelin toiminnot on jaoteltu metodeiksi ``Pelialusta``-luokan alle.

algoritmi.py: Tiedostossa on MinMax-algoritmi alpha beta karsinnalla. Tiedostossa on toteutettuna ``Algoritmi``-luokka, jota kutsutaan käynnistystiedostosta (main.py) vain silloin, jos pelaajaksi on valittu tekoäly. Tiedostosta kutsutaan pelin toiminnallisuuksia sisältävää ``Pelialusta``-luokkaa ja sen metodeita.

## MinMax-algoritmin aikavaativuus
MinMax-algoritmin aikavaativuus O(bm), jossa b on pelin haarautuva tekijä ja m vastaa maksimi solmujen syvyyttä. Algoritmi suorittaa DFS:n eli Depth-first search, jossa se aloittaa juurisolmusta ja etenee niin pitkälle kuin on mahdollista jokaisessa haarassa ennen takaisin tuloa. Alpha beta karsinnalla taas yritetään tehostaa MinMaxia niin, että yritetään laskea oikea MinMax käymättä kuitenkaan jokaisessa solmussa. Jolloin mahdollisesti useampi haara voidaan jättää huomioitta eli karsia. Algoritmi etsiikin kaksi arvoa; alphan (Max-solmut) ja betan (Min-solmut.)

Pahimmassa mahdollisessa tapauksessa eli, mikäli ei ole solmua, jota karsia pois, käydään kaikki haarat läpi. Tässä pelissä syvyydeksi on asetettu 5, sillä se oli suositeltu syvyys 2048-peliin. Parhaimmassa tapauksessa jokainen solmu arvioi 2b - 1 "lapsenlapsen" päätettäkseen sen arvon. Huonoimmassa tapauksessa solmu arvioi b^2 "lapsenlapsen". Tästä voidaan päätellä, että MinMax yhdistettynä Alpha beta karsinnalla arvioi O(b^(syvyys/2)) solmua. 

### Suorituskykytestaus
Tässä aiheessa suorituskykytestausta ei vaadittu. 

## Työn mahdolliset puutteet ja parannusehdotukset
Olisihan peli paremman näköinen mikäli se olisi toteutettu graafisena käyttöliittymänä. Tosin tässä pelissä myös tekstikäyttöliittymä on mielestäni tarpeeksi, koska pelataan vain numeroin ja siirrot tapahtuvat wasd-näppäimistä.
Pelin luonteen vuoksi testaus on hankalaa, mutta tätä yritetty kuitenkin monipuolistaa toteuttamalla erilaisia pelialustoja.

## Lähteet

Temple University. 2003. Lecture 7. Luettu: 9.12.2022. https://cis.temple.edu/~vasilis/Courses/CIS603/Lectures/l7.html.

Wikipedia. 2022. Minimax. Päivitetty: 23.11.2022. Luettu 10.12.2022. https://en.wikipedia.org/wiki/Minimax.

