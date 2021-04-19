import uuid

class Riddle:

    def __init__(self, content, answer, id=None):

        self.content = content
        self.answer = answer
        self.id = id or str(uuid.uuid4())

    def __str__(self):
        return str(self.answer)

    def __repr__(self):
        return str(self)
 
