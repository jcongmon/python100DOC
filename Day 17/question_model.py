class Question:
    def __init__(self, q, a):
        self.text = q
        self.answer = a

    def get_question(self):
        return self.text

    def get_answer(self):
        return self.answer
