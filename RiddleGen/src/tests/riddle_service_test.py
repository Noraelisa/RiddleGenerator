import unittest
from entities.riddle import Riddle
from services.riddle_service import (RiddleService)

class FakeRiddleRepository:
    def __init__(self, riddles=None):
        self.riddles = riddles or []

    def find_all(self):
        return self.riddles

    def create(self, riddle):
        self.riddles.append(riddle)

        return riddle

    def delete_all(self):
        self.riddles = []

class TestRiddleService(unittest.TestCase):
    def setUp(self):
        self.riddle_service = RiddleService(FakeRiddleRepository())

        self.riddle_test_three = Riddle("Am I the third riddle?", "Yes")
        self.riddle_test_four = Riddle("Am I the fourth riddle?", "Yes")

    def test_create_riddle(self):
        self.riddle_service.create_riddle("Am I a riddle", "Yes")
        riddles = self.riddle_service.get_riddles()

        self.assertEqual(len(riddles), 1)
        self.assertEqual(riddles[0].content + riddles[0].answer,
                        "Am I a riddle" + "Yes")

    def test_get_riddles(self):
        self.riddle_service.create_riddle(self.riddle_test_three.content,
                                        self.riddle_test_three.answer)
        self.riddle_service.create_riddle(self.riddle_test_four.content,
                                        self.riddle_test_four.answer)

        all_riddles = self.riddle_service.get_riddles()

        self.assertEqual(len(all_riddles), 2)
        self.assertEqual(all_riddles[0].content + all_riddles[0].answer,
                        self.riddle_test_three.content + self.riddle_test_three.answer)

        self.assertEqual(all_riddles[1].content + all_riddles[1].answer,
                        self.riddle_test_four.content + self.riddle_test_four.answer)
