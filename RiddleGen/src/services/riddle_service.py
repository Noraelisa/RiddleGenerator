from entities.riddle import Riddle

from repositories.riddle_repository import (
    riddle_repository as default_riddle_repository)

class RiddleService:
    def __init__(self, riddle_repository=default_riddle_repository):
        self._riddle_repository = riddle_repository

    def create_riddle(self, content, answer):
        riddle = Riddle(content=content, answer=answer, riddle_id=None)

        return self._riddle_repository.create(riddle)

    def get_riddles(self):

        return self._riddle_repository.find_all()

riddle_service = RiddleService()
