import unittest
from repositories.riddle_repository import riddle_repository
from entities.riddle import Riddle

class TestRiddleRepository(unittest.TestCase):
    def setUp(self):
        riddle_repository.delete_all()
        self.riddle_test_one = Riddle("Am I the first riddle?", "Yes")
        self.riddle_test_two = Riddle("Am I the second riddle?", "Yes")

    def test_create(self):
        riddle_repository.create(self.riddle_test_one)
        riddles = riddle_repository.find_all()

        self.assertEqual(len(riddles), 1)
        self.assertEqual(riddles[0].content + riddles[0].answer,
                        self.riddle_test_one.content +
                        " Answer is " + self.riddle_test_one.answer +
                        ", id: " + self.riddle_test_one.riddle_id)

    def test_find_all(self):
        riddle_repository.create(self.riddle_test_one)
        riddle_repository.create(self.riddle_test_two)

        riddles = riddle_repository.find_all()

        self.assertEqual(len(riddles), 2)
        self.assertEqual(riddles[0].content + riddles[0].answer,
                        self.riddle_test_one.content +
                        " Answer is " + self.riddle_test_one.answer +
                        ", id: " + self.riddle_test_one.riddle_id)
        self.assertEqual(riddles[1].content + riddles[1].answer,
                        self.riddle_test_two.content +
                        " Answer is " + self.riddle_test_two.answer +
                        ", id: " + self.riddle_test_two.riddle_id)
                        