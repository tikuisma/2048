# Vaatimusmäärittely

## Pelin tarkoitus

2048-pelin tarkoituksena on liu’uttaa ilmestyviä palikoita niin, että saadaan palikassa olevaa lukumäärää kasvatettua. Peli on yksinpeli ja sen pelialustana toimii 4 x 4 oleva ruudukko. Peliin ilmestyy aina palikka satunnaisesti mihin tahansa tyhjään olevaan ruutuun jokaisen tehdyn siirron jälkeen. Satunnainen palikka on numeroltaan joko 2 tai 4. Peliin ilmestyy 90 % todennäköisyydellä numero 2 ja 10 % todennäköisyydellä numero 4. Pelissä siirrytään vetämällä palikoita joko vasemmalle, oikealle, ylös tai alas. Mikäli vierekkäiset numerot ovat samat, palikat yhdistyvät ja pistemäärä plussaantuu eli esimerkiksi 4 + 4 tulee yksi kuutiopalikka, jossa on luku 8. Mikäli pelaaja yrittää liikkua suuntaan, jossa pelilaudalla ei tapahtuisi mitään, pelaajan tulee tehdä siirto uudelleen. Pelaajan kerättyä kuutiopalikka, jossa on luku 2048, on päässyt pelin läpi ja peli päättyy.

![image](https://user-images.githubusercontent.com/93583969/200129692-23c3b1ca-a204-416b-8e20-13d792ecab16.png)
(Kuva: Statt 2014)

Pelin tekeminen on osa Tietojenkäsittelytieteen kandidaatin (TKT) opintoja.

## Käyttöliittymä

Pelin käyttöliittymän tyyppi tulee olemaan tekstipohjainen.


## Sovelluksen toiminnallisuus

### Pelin aloitus ja kulku

Alussa valitaan pelaaja ja se on joko ihmispelaaja tai tekoäly. Valinnan jälkeen avautuu 4 x 4 oleva ruudukko, johon on asetettu yksi palikka satunnaisesti ja palikan numero on joko 2 tai 4. Mikäli peliä pelaa ihmispelaaja, hän valitsee palikalle suunnan nuolinäppäimillä. Mikäli pelaajana on tekoäly, tekee se valinnan itse. Peliä pelataan niin kauan, kunnes peliin on saatu 2048 palikka tai, peli on hävitty eli pelissä kaikki ruudut ovat täynnä ja palikoita ei pysty enää yhdistämään toisiinsa.

### Pelin päätyttyä

Mikäli peli on pelattu onnistuneesti läpi. Tarkastetaan pelaajan tekemien siirtojen määrä.
Tekoälyn pelin jälkeen tulostetaan pelatut kierrokset ja näiden mahdolliset voitot.

Ihmispelaajan sekä tekoälyn peli loppuu joko häviämiseen tai 2048 tulokseen. Peliä ei voi jatkaa, vaikka sen olisi onnistuneesti läpäissyt.


## Käytettävät kielet

Pelin ohjelmointikielenä käytetään Pythonia.

Projektin dokumentaatio, koodi ja kommentit tulevat olemaan suomen kielellä.

## Algoritmi ja tietorakenne

Käytän pelin tekemiseen Minimax-algoritmia, jota tehostetaan Alpha beta karsinta -algoritmilla. Se siis karsii siirtovaihtoehtoja pois, jotta kaikkia eri skenaarioita ei tarvitse käydä läpi (Zadrozny 2018). Vaikka pelissä ei virallisesti ole kahta pelaajaa, voi peliä ajatella ns. kaksinpelinä (Lazar 2020). Siksi MinMax-algoritmi sopii pelissä hyvin käytettäväksi. Pelaajan tavoitteenahan on maksimoida pisteensä pelissä ja satunnaisesti tulevia palikoita voidaan taas pitää ns. vihollisena, sillä sen voi ajatella yrittävän sijoittaa tulevia palikoita mahdollisimman huonoihin kohtiin oman pelin kannalta. Pelin algoritmiin on vielä lisätty painotettu pelialusta eli tekoälyn pelatessa pelin arvot painottuisivat vasempaan ylänurkkaan. Tehostaminen saadaan aikaan, kun verrataan vierekkäisiä numeroita ja pyritään valitsemaan pienin mahdollinen erotus sekä saadut arvot jaetaan vielä täysien ruutujen määrällä, jotta painotus kohdistuisi tyhjiin eli vapaisiin paikkoihin.

### Aikavaativuus

Algoritmia yritetty tehostaa painotetulla pelilaudalla.

## Lähteet

Lazar, D. 2020. How to apply Minimax to 2048. Päivitetty: 27.9.2020. Luettu: 5.11.2022. Saatavissa: [How to apply Minimax to 2048 (towardsdatascience.com)](https://towardsdatascience.com/playing-2048-with-minimax-algorithm-1-d214b136bffb).

Statt, N. 2014. 2048 starts easy; gets hard. Here's how to make it easy again. Päivitetty: 22.3.2014. Luettu: 5.11.2022. Saatavissa: [2048 starts easy; gets hard. Here's how to make it easy again (cnet.com)](https://www.cnet.com/tech/gaming/2048-starts-easy-gets-hard-heres-how-to-make-it-easy-again/).

Zadrozny, B. 2018. Beginner's guide to AI and writing your own bot for the 2048 game. Päivitetty: 10.10.2018. Luettu: 5.11.2022. Saatavissa: [Beginner's guide to AI and writing your own bot for the 2048 game (medium.com)](https://medium.com/@bartoszzadrony/beginners-guide-to-ai-and-writing-your-own-bot-for-the-2048-game-4b8083faaf53).
