import uuid

class Riddle:
    """Luokka, joka kuvaa yksittäistä arvoitusta

    Attributes:
        content: Merkkijonoarvo, joka kuvaa arvoituksen sisältöä.
        answer: Merkkijonoarvo, joka kuvaa arvoituksen vastausta.
        riddle_id: Merkkijonoarvo, joka kuvaa tehtävän id:tä
    """

    def __init__(self, content, answer, riddle_id=None):
        """Luokan konstruktori, joka luo uuden arvoituksen.

        Args:
            content: Merkkijonoarvo, joka kuvaa arvoituksen sisältöä.
            answer: Merkkijonoarvo, joka kuvaa arvoituksen vastausta.
            riddle_id:
                    Merkkijonoarvo, joka kuvaa arvoituksen id:tä.
                    Oletusarvoltaan generoitu uuid.
        """

        self.content = content
        self.answer = answer
        self.riddle_id = riddle_id or str(uuid.uuid4())

    def __str__(self):
        """Muodostaa arvoituksesta merkkijonomuotoisen esityksen.

        Returns:
            Merkkijono, joka kertoo arvoituksen ja sen vastauksen.
        """

        return str(self.content) + str(self.answer)

    def __repr__(self):
        """Muodostaa kaikista arvoituksista yksiselitteisen merkkijonomuotoisen esityksen listana.

        Returns:
            Merkkijono, joka kertoo arvoituksen ja sen vastauksen.
        """

        return str(self)
