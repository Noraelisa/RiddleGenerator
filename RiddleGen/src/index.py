from tkinter import Tk
from config import RIDDLES_FILENAME
from repositories.riddle_repository import riddle_repository
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
#riddle_repository.create(Riddle("What has roots as nobody sees, is taller than trees, up, up, up it goes, and yet, never grows?", "Mountain")) # pylint: disable=line-too-long
#riddle_repository.create(Riddle("Thirty white horses on a red hill. First they champ,then they stamp, then they stand still.", "Teeth")) # pylint: disable=line-too-long
#riddle_repository.create(Riddle("Voiceless it cries, wingless flutters,toothless bites, mouhless mutters.", "Wind")) # pylint: disable=line-too-long
#riddle_repository.create(Riddle("An eye in a blue face. Saw an eye in a green face. 'That eye is like to this eye' Said the first eye, But in low place, Not in high place.", "The Sun")) # pylint: disable=line-too-long

#riddle_repository.create(Riddle("It cannot be seen, cannot be felt, Cannot be heard, cannot be smelt. It lies behind stars and under hills, And empty holes it fills. It comes first and follows after, Ends life, kills laughter.", "Dark")) # pylint: disable=line-too-long
#print(RIDDLES_FILENAME)
#print(riddle_repository.find_all())
#riddle_repository.delete_all()
