from config import RIDDLES_FILENAME
from repositories.riddle_repository import riddle_repository
from entities.riddle import Riddle

print(RIDDLES_FILENAME)

riddle_repository.create(Riddle("Learn the repository pattern"))

riddles = riddle_repository.find_all()

print(riddles)
