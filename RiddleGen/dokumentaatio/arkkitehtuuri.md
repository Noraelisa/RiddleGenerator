# Arkkitehtuurikuvaus

## Rakenne ja sovelluslogiikka 

### Sovelluksen koodin rakenne on seuraava:

![Pakkauskaavio](./photos/RiddleGen_pakkauskaavio.png)

- Pakkaus ui: käyttöliittymään liittyvä koodi
- Pakkaus services: sovelluslogiikkaan liittyvä koodi
- Pakkaus repositories: tietojen pysyväistallennukseen liittyvä koodi
- Pakkaus entities: luokka, joka kuvastaa sovelluksen käyttämää tietokohdetta

### Luokkakaavio: Riddle

- Kuvaa arvoituksen sisältöä, vastausta ja id:tä

![Luokkakaavio](./photos/Riddle_luokkakaavio.png)

### Sovelluslogiikka

- Sovelluksen osien suhteita kuvaava kaavio:

![Sovelluslogiikka](./photos/RiddleGen_sovelluslogiikka2.png)

## Toiminnallisuudet

- Arvoituksen luominen tapahtuu hypoteettisesti painamalla "Create"-nappia: 

![Sekvenssikaavio](./photos/RiddleGen_sekvenssikaavio.png)

## Tietojen pysyväistallennus

- Sovellus tallentaa tietoa CSV-tiedostoon (riddles.csv) ja se tallentuu seuraavassa muodossa:

Ensimmäisenä arvoituksen id, sitten itse arvoitus, ja viimeisenä arvoituksen vastaus
