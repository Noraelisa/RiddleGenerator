from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        welcome_label = ttk.Label(master=self._root,
                                text="I am a Riddler Generator, Welcome!")
        info_label = ttk.Label(master=self._root,
                                text="Here you can make your own riddle and become a true riddler")
        riddle_entry = ttk.Entry(master=self._root)
        send_button = ttk.Button(master=self._root, text="Send")

        welcome_label.grid(columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)
        info_label.grid(columnspan=2,
                            row=1, column=0,
                            sticky=(constants.S),
                            padx=5, pady=5)
        riddle_entry.grid(columnspan=2,
                            row=2, column=0,
                            sticky=(constants.S), padx=5,
                            pady=5, ipadx=50)
        send_button.grid(row=3, column=0,
                            columnspan=2,
                            sticky=(constants.S),
                            padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=500)

window = Tk()
window.title("RiddlerGen")

ui = UI(window)
ui.start()

window.mainloop()
