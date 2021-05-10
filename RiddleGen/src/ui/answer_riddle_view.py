from tkinter import ttk, constants

class AnswerView:
    def __init__(self, root, handle_main_view):
        self._root = root
        self._handle_main_view= handle_main_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        answer_label = ttk.Label(master=self._frame, text="Answer from db comes here...wrong/right")

        start_button = ttk.Button(master=self._frame,
                                text="Go back to the start and try again",
                                command=self._handle_main_view)

        answer_label.grid(row=3, column=0,
                            columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)
        start_button.grid(row=6, column=0,
                            columnspan=2,
                            sticky=(constants.S),
                            padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=500)
