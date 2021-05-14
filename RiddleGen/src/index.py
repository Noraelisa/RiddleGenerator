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
