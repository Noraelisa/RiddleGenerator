# ot-harjoitustyo

## RiddleGen

RiddleGen on arvoitusgeneraattori, joka arpoo käyttäjälle arvoituksen, johon käyttäjä vastaa. Käyttäjä saa tietää onko vastaus oikein vai väärin. Käyttäjällä on myös mahdollisuus lisätä itse arvoituksia arvoitusgeneraattoriin. RiddleGeniin on lisätty valmiiksi arvoituksia, jotka arvotaan käyttäjälle satunnaisesti. 

### Dokumentaatio

- [Työaikakirjanpito](https://github.com/Noraelisa/ot-harjoitustyo/blob/main/RiddleGen/dokumentaatio/tyoaikakirjanpito.md)

- [Vaatimusmäärittely](https://github.com/Noraelisa/ot-harjoitustyo/blob/main/RiddleGen/dokumentaatio/vaatimusmaarittely.md)

- [Arkkitehtuurikuvaus](https://github.com/Noraelisa/ot-harjoitustyo/blob/main/RiddleGen/dokumentaatio/arkkitehtuuri.md)
- 
### Asennus

    - Huomioi, että olet RiddleGen-hakemistossa
    - Riippuvuuksien asentaminen: poetry install
    - Sovellus käynnistyy: poetry run invoke start
     
### Komentorivitoiminnot
  
    - Ohjelmansuoritus: poetry run invoke start
    - Testaus: poetry run invoke test 
    - Testikattavuusraportin generointi: poetry run invoke coverage-report
    - Pylint tarkistukset: poetry run invoke lint 
    
- [Pylint määritelmät](https://github.com/Noraelisa/ot-harjoitustyo/blob/main/RiddleGen/.pylintrc)

### Projektin eteneminen

  ## Viikko 3

    - Projekti on aloitettu ja sille on luotu perusta 
    - Graaffistakäyttöliittymää on aloitettu ja se löytyy ui.py tiedostosta
    - Tietokantayhteyden luonti on aloitettu ja valmiita arvoituksia on alettu lisäämään. Yhteys ei toimi vielä oikein
    - Testien teko ei vielä onnistunut, sillä en saanut projektin toimintoja toimimaan ajallaan

  ## Viikko 4
  
    - Viime viikosta projekti on edennyt hyvin ja sovellusta on laajennettu
    - Graaffistakäyttöliittymää on aloitettu ja se löytyy ui-hakemistosta
    - Pääikkuna on luotu ja sen voi avata poetry run invoke start-komennolla
    - Käyttäjälle myös aukeaa ensimmäinen ikkuna
    - Tietokantayhteyden luonti on onnistunut ja yhteys toimii 
    - Valmiita arvoituksia ja niihin vastauksia on lisätty datahakemiston riddles.csv-tiedostoon
    - Testaaminen on aloitettu
    - Testien haarautumakattavuus on 47% tällä hetkellä
    - Sovellukselle pystytään generoimaan testikattavuusraportti
    - Pylint on otettu käyttöön (10/10)
    - Alustava rakenne luotu

  ## Viikko 5
  
    - Graafistakäyttöliittymää on laajennettu useaan näkymään
    - Poistettu aloitettu yhteys sqliteen ja korjattu riddle.csv-tiedoston yhteys
    - Sovelluslogiikka ja käyttöliittymä erotettu luomalla service-hakemisto
    - Poistettu .gitignoresta pytest.ini-tiedosto, joten yhteys .env-tiedostoon näkyy
    - Pylint 9.86/10
    - Testien haarautumakattavuus on 94% tällä hetkellä
    - Sovellukselle pystytään generoimaan testikattavuusraportti
    - Kerrosrakennetta muutettu service-tiedoston luomisen myötä
    - Issuet sallittu
- [GitHub release](https://github.com/Noraelisa/ot-harjoitustyo/releases/tag/viikko5)

  

