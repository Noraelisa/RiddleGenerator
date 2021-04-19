from config import RIDDLES_FILENAME
from repositories.riddle_repository import riddle_repository
from entities.riddle import Riddle

riddle_repository.create(
                    Riddle("""What has roots as nobody sees, is taller than trees,
                        up, up, up it goes, and yet, never grows?""",
                        "Mountain"))
riddle_repository.create(
                    Riddle("""Thirty white horses on a red hill. First they champ,
                        then they stamp, then they stand still.""",
                        "Teeth"))
riddle_repository.create(
                    Riddle("""Voiceless it cries, wingless flutters,
                        toothless bites, mouhless mutters.""",
                        "Wind"))
riddle_repository.create(
                    Riddle("""An eye in a blue face. Saw an eye in a green face.
                        'That eye is like to this eye' Said the first eye,
                        But in low place, Not in high place""",
                        "The Sun"))
