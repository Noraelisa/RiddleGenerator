# Käyttöohje

## Ohjelman käynnistys

- Ensin asenna riippuvuudet komennolla:

```
poetry install
```

- Tämän jälkeen voit käynnistää sovelluksen komennolla:

```
poetry run invoke start
```
- Kun on suoritettu edellä mainitut komennot, aukeaa sovelluksen graafinenkäyttöliittymä

![MainView](./photos/RiddleGen_MainView.png)

- "Write a riddle here"-napista voi siirtyä seuraavaan näkymään kirjoittamaan arvoituksen, joka tallentuu riddles.csv-tiedostoon

![WriteView](./photos/RiddleGen_WriteView.png)

- "Guess a riddle here"-napista voi siirtyä seuraavaan näkymään arvaamaan arvoitusta

![GuessView](./photos/RiddleGen_GuessView.png)

- Arvoituksen vastaus kirjoitetaan tekstikenttään ja arvaus lähetetään painamalla "Guess"-nappia
- Jos "Guess"-nappia painaa ilman, että on syöttänyt tekstikenttään mitään, niin sovellus lataa näkymän uudelleen ja arvoitus vaihtuu toiseen
- Jos arvoitus on liian vaikea, on mahdollisuus saada yksi vinkki "Hint"-napista. Nappi tulostaa käyttäjän näkymään arvoituksen ensimmäisen kirjaimen

![HintView](./photos/RiddleGen_GuessView_hint.png)

- Jos arvoitus arvataan oikein, siirtyy näkymä seuraavaan

![CorrectView](./photos/RiddleGen_correct.png)

- Jonka jälkeen "Go back to the start"-nappi vie aloitusnäkymään

- Jos arvoituksen arvaus osoittautuu vääräksi, siirtyy näkymä seuraavaan

![IncorrectView](./photos/RiddleGen_incorrect.png)

 - Jonka jälkeen "Go back to the start and try again"-nappi vie aloitusnäkymään

 - Jos käyttäjä ei arvaa arvoitusta oikein, sovellus ei missään vaiheessa myöskään paljasta arvoitusta. Vain, että onko vastaus oikein vai väärin.
