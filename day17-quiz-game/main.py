import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in data.question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")