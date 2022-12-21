# Testausdokumentti
Ohjelmaa on testattu automatisoiduilla unittest-testeillä sekä manuaalisesti tekstikäyttöliittymässä. Pelin algoritmin testaaminen on hankalaa, koska peli on hyvin satunnainen ja mahdollisia tapahtumaketjuja on todella paljon. Pelissä on mukana muun muassa satunnaisuutta, jonka takia on myös hankalaa määrittää algoritmilla pelatessa, että mikä on juuri oikea siirto pelialustalla. Pelissä ei myöskään ole niin selvää "oikeaa" ja "väärää" siirtoa, joten tämä ei ole niin yksiselitteistä.

## Yksikkö- ja integraatiotestaus
### Repositorio-luokat
Repositorio-luokkaa ``Pelialusta`` testataan antamalla sille oma generoitu pelialusta ja tällä testataan luokan metodeita.

Repositorio-luokkaa ``Algoritmi`` testataan antamalla erilaisia pelialustoja eli näissä on lukuja, jotta voidaan tarkistaa onko metodien palauttama arvo oikea. 

### Testauskattavuus
Testauskattavuus on seuraavanlainen:
file:///home/tikuisma/Pictures/Screenshots/Screenshot%20from%202022-12-21%2020-02-59.png
Testauskattavuutta pystyy tarkistelemaan paremmin ajettua testit ja katsomalla ne htmlcov:n ``index.html``-tiedostosta.
Testauskattavuusraportin voit katsoa täältä: [Codecov](https://app.codecov.io/gh/tikuisma/2048).

## Järjestelmätestaus
Pelin käynnistystiedostoa ``main.py`` on hankala testata unittestein, sillä se on ns. pelin käyttöliittymä. Siksi käynnistystiedosto onkin testattu manuaalisesti tekstikäyttöliittymässä.

### Asennus ja konfigurointi
Pelin [käyttöohjeessa](https://github.com/tikuisma/2048/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md) on pelin asennuksesta tarkemmin sekä pelin pikakäyttöopas.
Peliä on testattu ainoastaan Linux-ympäristössä.