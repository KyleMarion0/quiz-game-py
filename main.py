from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question['text'], question['answer']) for question in question_data]
#print(question_bank[0].text)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.q_number}")