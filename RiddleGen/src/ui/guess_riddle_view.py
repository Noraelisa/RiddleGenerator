from tkinter import ttk, constants
from services.riddle_service import riddle_service

class RiddleView:
    def __init__(self, root, riddle):
        self._root = root
        self._riddle = riddle
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
        self._initialize_riddle_item(self._riddle)

class GuessView:
    def __init__(self, root, handle_correct_answer_view,
                handle_incorrect_answer_view, handle_riddle_guess):
        self._root = root
        self._handle_correct_answer_view = handle_correct_answer_view
        self._handle_incorrect_answer_view = handle_incorrect_answer_view
        self._frame = None
        self._riddle_answer_entry = None
        self._riddle_frame = None
        self._riddle_view = None
        self._current_riddle = riddle_service.get_random_riddle()
        self._handle_riddle_guess = handle_riddle_guess

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_riddle(self):
        if self._riddle_view:
            self._riddle_view.destroy()

        self._current_riddle = riddle_service.get_random_riddle()

        self._riddle_view = RiddleView(self._riddle_frame, self._current_riddle)

        self._riddle_view.pack()

    def _initialize_riddle_answer_field(self):
        riddle_label = ttk.Label(master=self._frame, text="Write your answer here:")
        self._riddle_answer_entry = ttk.Entry(master=self._frame)

        riddle_label.grid(row=4, column=0,
                            columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)
        self._riddle_answer_entry.grid(columnspan=2,
                            row=5, column=0,
                            sticky=(constants.S), padx=5,
                            pady=5, ipadx=50)

    def _func_guess(self):
        users_guess = riddle_service.guess_riddle(self._current_riddle,
                                            self._riddle_answer_entry.get())

        if len(self._riddle_answer_entry.get()) == 0:
            return self._handle_riddle_guess()
        elif users_guess is True:
            return self._handle_correct_answer_view()
        else:
            return self._handle_incorrect_answer_view()

    def _func_hint(self):
        riddle_hint_text = ttk.Label(master=self._frame, text="The first letter is:")
        riddle_hint = ttk.Label(master=self._frame, text=self._current_riddle.answer[0])
        riddle_hint_text.grid(row=8, column=0,
                            columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)
        riddle_hint.grid(row=9, column=0,
                            columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._riddle_frame = ttk.Frame(master=self._frame)

        self._initialize_riddle()
        self._initialize_riddle_answer_field()

        riddle_label = ttk.Label(master=self._frame, text="The riddle:")

        riddle_label.grid(row=0, column=0,
                            columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)
        guess_button = ttk.Button(master=self._frame,
                                text="Guess",
                                command=self._func_guess)
        hint_button = ttk.Button(master=self._frame,
                                text="Hint",
                                command=self._func_hint)
        self._riddle_frame.grid(row=2, column=0,
                            columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)
        guess_button.grid(row=6, column=0,
                            columnspan=2,
                            sticky=(constants.S),
                            padx=5, pady=5)
        hint_button.grid(row=7, column=0,
                            columnspan=2,
                            sticky=(constants.S),
                            padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)
