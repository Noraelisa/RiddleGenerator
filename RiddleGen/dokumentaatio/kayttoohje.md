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

- "Guess a riddle here"-napista voi siirtyä seuraavaan näkymään arvaamaan arvoitusta (arvaaminen ei ole vielä toiminnassa)

![GuessView](./photos/RiddleGen_GuessView.png)
