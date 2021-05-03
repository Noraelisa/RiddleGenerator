from entities.riddle import Riddle

from repositories.riddle_repository import (
    riddle_repository as default_riddle_repository)

class RiddleService:
    """Sovelluslogiikasta vastaava luokka.
    """

    def __init__(self, riddle_repository=default_riddle_repository):
        """Luokan konstruktori, joka luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            riddle_repository: Oletusarvoltaan RiddleRepository-olio,
            jolla on RiddleRepository-luokkaa vastaavat metodit.
        """

        self._riddle_repository = riddle_repository

    def create_riddle(self, content, answer):
        """Luo uuden arvoituksen.

        Args:
            content: Merkkijonoarvo, joka kuvaa arvoituksen sisältöä.
            answer: Merkkijonoarvo, joka kuvaa arvoituksen vastausta.

        Returns:
            Luotu arvoitus Riddle-olion muodossa.
        """

        riddle = Riddle(content=content, answer=answer, riddle_id=None)

        return self._riddle_repository.create(riddle)

    def get_riddles(self):
        """Palauttaa tietokantaan lisätyt arvoitukset.

        Returns:
            Palauttaa tietokantaan lisätyt arvoitukset Riddle-olioiden listana.
        """

        return self._riddle_repository.find_all()

    def get_riddle(self):
        """Palauttaa tietokantaan lisätyn arvoituksen.

        Returns:
            Palauttaa tietokantaan lisätyn arvoituksen Riddle-oliona
        """
            
        return self._riddle_repository.get_riddle()    

riddle_service = RiddleService()
