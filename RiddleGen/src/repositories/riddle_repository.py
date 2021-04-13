from entities.riddle import Riddle
import os
from pathlib import Path

class RiddleRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self._read()

    def create(self, riddle):
        riddles = self.find_all()

        riddles.append(riddle)

        self._write(riddles)

        return riddle    

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        riddles = []

        self._ensure_file_exists()

        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                id = parts[0]
                content = parts[1]
                
                riddles.append(
                    Riddle(id, content)
                )

        return riddles

    def _write(self, riddles):
        self._ensure_file_exists()

        with open(self._file_path, "w") as file:
            for riddle in riddles:
           
                row = f"{riddle.id};{riddle.content}"

                file.write(row+"\n")    


dirname = os.path.dirname(__file__)

riddle_repository = RiddleRepository(os.path.join("data", "riddles.csv"))
