from tkinter import ttk, constants

class MainView:
    def __init__(self, root, handle_riddle_write, handle_riddle_guess):
        self._root = root
        self._handle_riddle_write = handle_riddle_write
        self._handle_riddle_guess = handle_riddle_guess
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        welcome_label = ttk.Label(master=self._frame,
                                text="I am a Riddler Generator, Welcome!")
        info_label = ttk.Label(master=self._frame,
                                text="Here you can make your own riddle and become a true riddler or try to guess one!")
        write_button = ttk.Button(master=self._frame,
                            text="Write a riddle here",
                            command=self._handle_riddle_write)
        guess_button = ttk.Button(master=self._frame,
                                text="Guess a riddle here",
                                command=self._handle_riddle_guess)

        welcome_label.grid(columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)
        info_label.grid(columnspan=2,
                            row=1, column=0,
                            sticky=(constants.S),
                            padx=5, pady=5)
        write_button.grid(row=3, column=0,
                            columnspan=2,
                            sticky=(constants.S),
                            padx=5, pady=5)
        guess_button.grid(row=4, column=0,
                            columnspan=2,
                            sticky=(constants.S),
                            padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=500)
