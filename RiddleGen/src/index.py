from config import RIDDLES_FILENAME
from repositories.riddle_repository import riddle_repository
from entities.riddle import Riddle

print(RIDDLES_FILENAME)

riddle_repository.create(Riddle("What has roots as nobody sees, is taller than trees, up, up, up it goes, and yet, never grows?"))
riddle_repository.create(Riddle("Thirty white horses on a red hill. First they champ, then they stamp, then they stand still."))

riddles = riddle_repository.find_all()

print(riddles)
