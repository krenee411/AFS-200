import random

from dataclasses import dataclass


@dataclass
class TriviaQuestion:
    question: str
    category: str
    difficulty: str
    correct_answer: str
    incorrect_answers: list
    id: int

    def getQuestion(self):
        return self.question

    def setQuestion(self, question):
        self.question = question

    def getCorrectAnswer(self):
        return self.correct_answer

    def setCorrectAnswer(self, correct_answer):
        self.correct_answer = correct_answer

    def getIncorrectAnswer(self):
        return self.incorrect_answers
    
    def setIncorrectAnswer(self, incorrect_answers):
        self.incorrect_answers = incorrect_answers

    def getShuffledAnswers(self):
        answers =[]
        answers.append(self.correct_answer)
        for wrong in self.incorrect_answers:
            answers.append(wrong)
            random.shuffle(answers)
        return answers


