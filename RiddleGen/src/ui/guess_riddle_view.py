from tkinter import ttk, constants

class GuessView:
    def __init__(self, root, handle_main_view):
        self._root = root
        self._handle_main_view= handle_main_view
        self._frame = None
        self._riddle_answer_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_riddle_answer_field(self):
        riddle_label = ttk.Label(master=self._frame, text="Write your answer here")
        self._riddle_answer_entry = ttk.Entry(master=self._frame)

        riddle_label.grid(row=4, column=0,
                            columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)
        self._riddle_answer_entry.grid(columnspan=2,
                            row=5, column=0,
                            sticky=(constants.S), padx=5,
                            pady=5, ipadx=50)
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        riddle_label = ttk.Label(master=self._frame, text="Riddle from db comes here...")

        self._initialize_riddle_answer_field()

        guess_button = ttk.Button(master=self._frame, text="Guess", command=self._handle_main_view)

        riddle_label.grid(row=3, column=0,
                            columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)
        guess_button.grid(row=6, column=0,
                            columnspan=2,
                            sticky=(constants.S),
                            padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=500)
