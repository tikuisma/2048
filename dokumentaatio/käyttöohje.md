# Pelin käyttöohje
## Pikaohje pelin pelaamiseen
2048-peli on 4 x 4 ruudukko, jossa siirrytään ylös, alas, vasemmalle ja oikealle. Peliin ilmestyy aina ennen siirtoa numero, joka on joko 2 tai 4. Mahdollisuus numero 2 on 90 % ja numero 4 10 %. Pelin tarkoituksena on yhdistää palikat niin, että saat kerättyä palikan, joka on arvoltaan 2048.

Peli alkaa valinnalla siitä, että haluatko itse pelata 2048-peliä vai haluatko katsoa, kun tekoäly pelaa. Mikäli valitset pelata itse, on käytössäsi näppäimet WSAD, joista tapahtuvat siirrot pelialustalla. Peli päättyy joko häviöön tai voittoon. Pelialustalla ei voi yrittää tehdä siirtoa sellaiseen suuntaan, jossa pelialustalla ei mikään siirtyisi. Tässä tapauksessa sinun tulee siirtyä niihin suuntiin, joissa pelialustalla tapahtuu myös siirto/siirtoja.
Tekoälyn pelatessa voit valita pelikierrosten lukumäärän (numeerisena) sekä odotusajan sekunteina (kokonaisluku). Pelin loputtua näet voitot muodossa esim. "1 / 11" sekä kokonaisuudessaan käytetyn ajan pelien pelaamiseen.

Siirtymiset pelialustalla:

- W / w = Siirto ylös
- S / s = Siirto alas
- A / a = Siirto vasemmalle
- D / d = Siirto oikealle

Valitun siirron jälkeen tulee painaa Enter-näppäintä.

Katso tarkemmin pelistä [vaatimusmäärittelystä](https://github.com/tikuisma/2048/blob/master/dokumentaatio/vaatimusmaarittely.md).

## Asennus
1. Helpoin tapa on kloonata repo omalle koneellesi.
2. Asenna sitten repon riippuvuudet komennolla: ``poetry install``.
3. Siirry sitten src-kansion sisälle ja aja komento: ``python3 main.py``, jolloin peli lähtee käyntiin.

### Testien ajaminen
Testit saa suoritettua siirtymällä ensin virtuaaliympäristöön: ``poetry shell``, jonka jälkeen täytyy ajaa vielä komento: ``poetry run pytest``.

### Koodin laadun seuranta
Koodin laatua voi seurata ajamalla komennon: ``pylint src``.
Koodin laatupisteytys 22.12.: 9.45 / 10