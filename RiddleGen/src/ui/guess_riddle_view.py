from tkinter import ttk, constants
from services.riddle_service import riddle_service

class RiddleListView:
    def __init__(self, root, riddles):
        self._root = root
        self._riddles = riddles
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_riddle_item(self, riddle):
        riddle_frame = ttk.Frame(master=self._frame)
        riddle_label = ttk.Label(master=riddle_frame, text=riddle.content)

        riddle_label.grid(row=4, column=0,
                            columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)

        riddle_frame.grid_columnconfigure(0, weight=1)
        riddle_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for riddle in self._riddles:
            self._initialize_riddle_item(riddle)

class GuessView:
    def __init__(self, root, handle_answer_view):
        self._root = root
        self._handle_answer_view = handle_answer_view
        self._frame = None
        self._riddle_answer_entry = None
        self._riddle_list_frame = None
        self._riddle_list_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_riddle_list(self):
        if self._riddle_list_view:
            self._riddle_list_view.destroy()

        riddles = riddle_service.get_riddles()

        self._riddle_list_view = RiddleListView(self._riddle_list_frame, riddles)

        self._riddle_list_view.pack()

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
        self._riddle_list_frame = ttk.Frame(master=self._frame)


        self._initialize_riddle_list()
        self._initialize_riddle_answer_field()

        guess_button = ttk.Button(master=self._frame,
                                text="Guess",
                                command=self._handle_answer_view)

        self._riddle_list_frame.grid(row=3, column=0,
                            columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)
        guess_button.grid(row=6, column=0,
                            columnspan=2,
                            sticky=(constants.S),
                            padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)
