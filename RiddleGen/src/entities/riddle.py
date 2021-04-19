import uuid

class Riddle:

    def __init__(self, content, answer, riddle_id=None):

        self.content = content
        self.answer = answer
        self.riddle_id = riddle_id or str(uuid.uuid4())

    def __str__(self):
        return str(self.content) + str(self.answer)

    def __repr__(self):
        return str(self)
