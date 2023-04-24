from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

qb = QuizBrain(question_bank)

while qb.still_has_question():
    qb.input()

print("You've completed the quiz.")
print(f"The final score is {qb.get_score()}/{qb.get_q_num()}.")