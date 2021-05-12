from tkinter import Tk
from repositories.riddle_repository import riddle_repository
from services.riddle_service import riddle_service
from entities.riddle import Riddle
from ui.ui import UI

def main():
    window = Tk()
    window.title("RiddleGen")

    ui_main = UI(window)
    ui_main.start()

    window.mainloop()

if __name__ == '__main__':
    main()

# sallitaan ylipitkät rivit tässä tapauksessa
'''
riddle_repository.create(Riddle("What has roots as nobody sees, is taller than trees, up, up, up it goes, and yet, never grows?", "Mountain")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("Thirty white horses on a red hill. First they champ, then they stamp, then they stand still.", "Teeth")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("Voiceless it cries, wingless flutters, toothless bites, mouhless mutters.", "Wind")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("An eye in a blue face. Saw an eye in a green face. 'That eye is like to this eye' Said the first eye, but in low place, not in high place.", "Sun")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("It cannot be seen, cannot be felt, cannot be heard, cannot be smelt. It lies behind stars and under hills, And empty holes it fills. It comes first and follows after, ends life, kills laughter.", "Dark")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("A box without hinges, key, or a lid, yet golden treasure inside is hid.", "Egg")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("Alive without breath, as cold as death. Never thirsty, ever drinking, all in mail never clinking", "Fish")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("This thing all thing devour, birds, beasts, trees, flowers. Gnaws iron, bites steel. Grinds hard stones to meal. Slays kings, ruins town and beats high mountain down.", "Time")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("What has to be broken before you can use it?", "Egg")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("I’m tall when I’m young, and I’m short when I’m old. What am I?", "Candle")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("What is always in front of you but can’t be seen?", "Future")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("What gets wet while drying?", "Towel")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("The more of this there is, the less you see. What is it?", "Darkness")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I?", "Shadow")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("What gets bigger when more is taken away?", "Hole")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("It belongs to you, but other people use it more than you do. What is it?", "Name")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("What has a head and a tail but no body?", "Coin")) # pylint: disable=line-too-long
riddle_repository.create(Riddle("What building has the most stories?", "Library")) # pylint: disable=line-too-long
'''
#riddle_repository.delete_all()
