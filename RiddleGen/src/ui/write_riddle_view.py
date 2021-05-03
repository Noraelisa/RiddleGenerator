from tkinter import ttk, constants
from services.riddle_service import riddle_service

class WriteView:
    def __init__(self, root, handle_main_view):
        self._root = root
        self._handle_main_view= handle_main_view
        self._frame = None
        self._riddle_entry = None
        self._riddle_answer_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_riddle_field(self):
        riddle_label = ttk.Label(master=self._frame, text="Write your riddle here")
        self._riddle_entry = ttk.Entry(master=self._frame)
        self._riddle_answer_entry = ttk.Entry(master=self._frame)

        riddle_label.grid(columnspan=2,
                            sticky=constants.S,
                            padx=5, pady=5)

    def _handle_create_riddle(self):
        riddle_content = self._riddle_entry.get()
        riddle_answer = self._riddle_answer_entry.get()

        if riddle_content and riddle_answer:
            riddle_service.create_riddle(riddle_content, riddle_answer)
            self._riddle_entry.delete(0, constants.END)
            self._riddle_answer_entry.delete(0, constants.END)

    def _initialize_footer(self):
        self._riddle_entry = ttk.Entry(master=self._frame)
        self._riddle_answer_entry = ttk.Entry(master=self._frame)

        write_button = ttk.Button(master=self._frame, text="Write",
                                command=lambda:[self._func_write(), self._func_main()])

        self._riddle_entry.grid(columnspan=2,
                            row=2, column=0,
                            sticky=(constants.S), padx=5,
                            pady=5, ipadx=50)
        self._riddle_answer_entry.grid(columnspan=2,
                            row=3, column=0,
                            sticky=(constants.S), padx=5,
                            pady=5, ipadx=5)

        write_button.grid(row=4, column=0,
                            columnspan=2,
                            sticky=(constants.S),
                            padx=5, pady=5)
    def _func_write(self):
        self._handle_create_riddle()

    def _func_main(self):
        self._handle_main_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_riddle_field()
        self._initialize_footer()

        self._root.grid_columnconfigure(1, weight=1, minsize=500)
