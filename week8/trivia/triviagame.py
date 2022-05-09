import requests
import triviaquestion



class TriviaGame():
    def __init__(self):
        self.questions = []
        self.correctQuestions = []
        self.incorrectQuestions = []

    def getAllQuestions(self):
        return self.questions
    
    def getData(self,amount,cat):
        url = f"https://opentdb.com/api.php?amount={amount}&category={cat}&difficulty=easy&type=multiple"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            response_JSON = response.json()
            return response_JSON
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    def storeQuestions(self,jsonTriviaData):
        id = 0
        for currentQuestion in jsonTriviaData["results"]:
            question =  currentQuestion["question"]
            category = currentQuestion["category"]
            difficulty = currentQuestion["difficulty"]
            correct_answer = currentQuestion["correct_answer"]
            incorrect_answers =[]
            for wrongAnswer in currentQuestion["incorrect_answers"]:
                incorrect_answers.append(wrongAnswer)
                id += 1
            newTriviaQuestion = triviaquestion.TriviaQuestion(question, category, difficulty, correct_answer, incorrect_answers, "", id)
            self.questions.append(newTriviaQuestion)

    def setCorrectQuestion(self, correctQuestions):
        self.correctQuestions = correctQuestions
    
    def setIncorrectQuestion(self, incorrectQuestions):
        self.incorrectQuestions = incorrectQuestions





    # print(getData(0,3,22))