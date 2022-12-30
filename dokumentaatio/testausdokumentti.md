# Testausdokumentti
Ohjelmaa on testattu automatisoiduilla unittest-testeillä sekä manuaalisesti tekstikäyttöliittymässä. Pelin algoritmin testaaminen on hankalaa, koska peli on hyvin satunnainen ja mahdollisia tapahtumaketjuja on todella paljon. Satunnaisuus tuo mukanaan sen, että on hankalaa määrittää algoritmilla pelatessa, että mikä on juuri oikea siirto pelialustalla. Pelissä ei myöskään ole niin selvää "oikeaa" ja "väärää" siirtoa, joten tämä ei ole niin yksiselitteistä.

## Yksikkö- ja integraatiotestaus
### Repositorio-luokat
Repositorio-luokkaa ``Pelialusta`` testataan antamalla sille oma generoitu pelialusta ja tällä testataan luokan metodeita. Pelin eri toimivuuksia pyritty testaamaan mahdollisimman kattavasti erilaisilla pelialustoilla. Tarkistetaan, että palautetut arvot ovat halutunlaiset ja oikeat.

Repositorio-luokkaa ``Algoritmi`` testataan antamalla erilaisia pelialustoja eli näissä on lukuja, jotta voidaan tarkistaa onko metodien palauttama arvo oikea. Pyritty testaamaan MinMax-algoritmia mahdollisimman kattavasti antamalla erilaisia pelialustoja ja tekemällä näihin siirtoja sekä pelin satunnaisuuden vuoksi on itse määritelty mikä numero (2, 4) ilmestyy mahdollisimman huonoimpaan paikkaan. Pelialusta on painotettu hieman eri tavalla, joten tällä hetkellä algoritmi pyrkii tekemään siirtoja niin kauan, kunnes siirrot eivät ole enää mahdollisia eli se pyrkii pelaamaan 2048, mutta varsinkin loppuvaiheessa algoritmi saattaa valita ei-minimireitin lopputulokseen. Tällainen tilanne on esimerkiksi se, että kaksi 1024-palikkaa ovat vierekkäin, mutta jos muualla voidaan tehdä vielä siirtoja yhdistämällä palikoita, algoritmi ei priorisoi voittoa vaan muiden palikoiden yhdistymisiä. Huomionarvoista kuitenkin on, että algoritmi ei kuitenkaan häviä peliä, vaan sillä on kuitenkin "tieto" siitä, että nämä palikat siirtämällä tulee voitto. 

### Testauskattavuus
Testauskattavuus on seuraavanlainen:
![Screenshot from 2022-12-21 20-02-59](https://user-images.githubusercontent.com/93583969/208976522-d4eed046-ed9f-48f8-81d5-6036f5f41844.png)

Testauskattavuutta pystyy tarkistelemaan paremmin ajettua testit ja katsomalla ne htmlcov:n ``index.html``-tiedostosta.
Testauskattavuusraportin voit myös katsoa täältä: [Codecov](https://app.codecov.io/gh/tikuisma/2048).

## Järjestelmätestaus
Pelin käynnistystiedostoa ``main.py`` on hankala testata unittestein, sillä se on ns. pelin käyttöliittymä. Siksi käynnistystiedosto onkin testattu manuaalisesti tekstikäyttöliittymässä. Testattu muun muassa virheelliset syötteiden annot ja pelin siirtojen toimivuus. Mikäli pelissä yritetään siirtyä suuntaan, jossa mikään ei siirtyisi, tämä ei ole mahdollista vaan käyttäjälle ilmoitetaan, että suunta ei ole ok. Algoritmin pelausta seurattu ja varmistettu, että pelin voitettaessa annetaan oikeat tulokset ja peli päättyy. Pelin voittomahdollisuus on algoritmilla ajettuna noin 1/10 pelistä, tätä on testattu ajamalla useampi testi kerrallaan.

### Asennus ja konfigurointi
Pelin [käyttöohjeessa](https://github.com/tikuisma/2048/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md) on pelin asennuksesta tarkemmin sekä pelin pikakäyttöopas.
Peliä on testattu ainoastaan Linux-ympäristössä.
