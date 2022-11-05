# Vaatimusmäärittely

## Pelin tarkoitus

2048-pelin tarkoituksena on liu’uttaa ilmestyviä palikoita niin, että saadaan palikassa olevaa lukumäärää kasvatettua. Peli on yksinpeli ja sen pelialustana toimii 4 x 4 oleva ruudukko. Peliin ilmestyy aina palikka satunnaisesti mihin tahansa tyhjään olevaan ruutuun jokaisen tehdyn siirron jälkeen. Palikassa om aina numero 2 tai 4. Pelissä siirrytään vetämällä palikoita joko vasemmalle, oikealle, ylös tai alas. Mikäli vierekkäiset numerot ovat samat, palikat yhdistyvät ja pistemäärä plussaantuu eli esimerkiksi 4 + 4 tulee yksi kuutiopalikka, jossa on luku 8. Pelaajan kerättyä kuutiopalikka, jossa on luku 2048, on päässyt pelin läpi. Läpäistyään pelin, pelaaja voi halutessaan vielä jatkaa peliä tai lopettaa.

![image](https://user-images.githubusercontent.com/93583969/200129692-23c3b1ca-a204-416b-8e20-13d792ecab16.png)
(Kuva: Statt 2014)

Pelaajan siirtojen määrää seurataan pelin aikana. Mikäli pelaaja on pelannut pelin onnistuneesti läpi, pääsee pelaaja top 10 pelaajan joukkoon, mikäli se on tehnyt vähemmän siirtoja kuin listalla jo olevat pelaajat.

Pelin tekeminen on osa tietojenkäsittelytieteen kandidaatin (TKT) opintoja.

## Käyttöliittymä

Pelin käyttöliittymän tyyppi ei ole vielä varma, joko se on graafinen tai tekstipohjainen. (Tämä kohta tulee täydentymään vasta siinä kohtaa, kun sovellus etenee ja valinta on tehty.)


## Sovelluksen toiminnallisuus

### Pelin aloitus ja kulku

Alussa valitaan pelaaja ja se on joko ihmispelaaja tai tekoäly. Valinnan jälkeen avautuu 4 x 4 oleva ruudukko, johon on asetettu yksi palikka satunnaisesti ja palikan numero on joko 2 tai 4. Mikäli peliä pelaa ihmispelaaja, hän valitsee palikalle suunnan nuolinäppäimillä. Mikäli pelaajana on tekoäly, tekee se valinnan itse. Peliä pelataan niin kauan, kunnes peliin on saatu 2048 palikka tai, peli on hävitty eli pelissä kaikki ruudut ovat täynnä ja palikoita ei pysty enää yhdistämään toisiinsa.

### Pelin päätyttyä

Mikäli peli on pelattu onnistuneesti läpi. Tarkastetaan pelaajan tekemien siirtojen määrä. Mikäli siirtojen määrä alittaa top 10 -listalla olevien pelaajien siirrot, saa pelaaja syöttää oman nimen/nimimerkin, jonka jälkeen nimi siirtyy listalle. Pelissä ei siis ole sisäänkirjautumista, vaan päästessään parhaiden joukkoon, pelaaja saa syöttää nimensä siinä kohtaa. Tekoälyn päästessä listalle, lisätään se automaattisesti ja merkitään tekoälyn tulokseksi.

Mikäli ihmispelaaja on päässyt pelin läpi, saa hän jatkaa pelaamista vielä niin halutessaan. Näistä kertyneitä tuloksia ei kuitenkaan kerätä enää minnekään.

Tekoälyn peli loppuu joko häviämiseen tai 2048 tulokseen. Se ei voi jatkaa pelin pelaamista, vaikka olisi pelin läpäissytkin.


## Käytettävät kielet

Pelin ohjelmointikielenä käytetään Pythonia.

Projektin dokumentaatio, koodi ja kommentit tulevat olemaan suomen kielellä.

## Algoritmi ja tietorakenne

Käytän pelin tekemiseen Minimax-algoritmia, jota tehostetaan Alpha beta karsinta -algoritmilla. Se siis karsii siirtovaihtoehtoja pois, jotta kaikkia eri skenaarioita ei tarvitse käydä läpi (Zadrozny 2018). Vaikka pelissä ei virallisesti ole kahta pelaajaa, voi peliä ajatella ns. kaksinpelinä (Lazar 2020). Siksi minimax-algoritmi sopii pelissä hyvin käytettäväksi. Pelaajan tavoitteenahan on maksimoida pisteensä pelissä ja satunnaisesti tulevia palikoita voidaan taas pitää ns. vihollisena, sillä sen voi ajatella yrittävän sijoittaa tulevia palikoita mahdollisimman huonoihin kohtiin oman pelin kannalta.  

### Aika- ja tilavaativuudet 

Täydentyy projektin edetessä.

## Lähteet

Lazar, D. 2020. How to apply Minimax to 2048. Päivitetty: 27.9.2020. Luettu: 5.11.2022. Saatavissa: [How to apply Minimax to 2048 (towardsdatascience.com)](https://towardsdatascience.com/playing-2048-with-minimax-algorithm-1-d214b136bffb).

Statt, N. 2014. 2048 starts easy; gets hard. Here's how to make it easy again. Päivitetty: 22.3.2014. Luettu: 5.11.2022. Saatavissa: [2048 starts easy; gets hard. Here's how to make it easy again (cnet.com)](https://www.cnet.com/tech/gaming/2048-starts-easy-gets-hard-heres-how-to-make-it-easy-again/).

Zadrozny, B. 2018. Beginner's guide to AI and writing your own bot for the 2048 game. Päivitetty: 10.10.2018. Luettu: 5.11.2022. Saatavissa: [Beginner's guide to AI and writing your own bot for the 2048 game (medium.com)](https://medium.com/@bartoszzadrony/beginners-guide-to-ai-and-writing-your-own-bot-for-the-2048-game-4b8083faaf53).
