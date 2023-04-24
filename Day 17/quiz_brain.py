class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def inc_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def next_question(self):
        self.question_number += 1

    def get_q_num(self):
        return self.question_number

    def still_has_question(self):
        return self.get_q_num() < len(self.question_list)

    def get_q_list(self):
        return self.question_list

    def get_key(self):
        return self.get_q_list()[self.get_q_num()]

    def check_answer(self, ans):
        if self.get_key().get_answer() == ans:
            print("You got it right!")
            self.inc_score()
        else:
            print("You got it wrong.")
        print(f"The correct answer is {self.get_key().get_answer()}.")
        print(f"The current score is {self.get_score()}/{self.get_q_num() + 1}.")

    def input(self):
        q = self.get_key().get_question()
        ans = input(f"Q.{self.get_q_num() + 1}: {q} (True/False): ").title()
        self.check_answer(ans)
        self.next_question()
        print()



