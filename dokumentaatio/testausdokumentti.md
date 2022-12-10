# Testausdokumentti
Ohjelmaa on testattu automatisoiduilla unittest-testeillä.

## Yksikkö- ja integraatiotestaus
### Repositorio-luokat
Repositorio-luokkaa ``Pelialusta`` testataan antamalla sille oma generoitu pelialusta ja tällä testataan luokan metodeita.

Repositorio-luokkaa ``Algoritmi`` testataan antamalla erilaisia pelialustoja eli näissä on lukuja, jotta voidaan tarkistaa onko metodien palauttama arvo oikea. 

### Testauskattavuus
Testauskattavuusraportin voit katsoa täältä: [Codecov](https://app.codecov.io/gh/tikuisma/2048).

## Järjestelmätestaus
Pelin käyttöliittymän testaus on toteutettu manuaalisesti tekstikäyttöliittymässä.

### Asennus ja konfigurointi
Peliä on testattu ainoastaan Linux-ympäristössä.