from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    model_question=Question(question_text,question_answer)
    question_bank.append(model_question)


quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
