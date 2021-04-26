from ui.main_view import MainView
from ui.guess_riddle_view import GuessView
from ui.write_riddle_view import WriteView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_riddle_write(self):
        self._show_write_view()

    def _handle_riddle_guess(self):
        self._show_guess_view()

    def _show_write_view(self):
        self._hide_current_view()

        self._current_view = WriteView(
            self._root,
            self._show_main_view
        )

        self._current_view.pack()

    def _show_guess_view(self):
        self._hide_current_view()

        self._current_view = GuessView(
            self._root,
            self._show_main_view
        )

        self._current_view.pack()

    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._handle_riddle_write,
            self._handle_riddle_guess
        )

        self._current_view.pack()
