from flask import Flask, request, render_template

import triviaquestion 


from triviagame import TriviaGame 


app = Flask(__name__)

questionList = TriviaGame()
questionList.storeQuestions(questionList.getData(5,22))

@app.route("/",methods=["GET"])
def home():
    return render_template('questionPage.html',questions=questionList.getAllQuestions() )


@app.route("/score", methods=['POST'])
def score():
    correctQuestions = []
    incorrectQuestions = []
    for question in questionList.getAllQuestions():
        # print(question.id)
        # print (question.getCorrectAnswer())
        userAnswer = request.form.get(str(question.id))
        # print("this is the answer" + userAnswer)
        question.setUserAnswer(userAnswer)
        if question.getCorrectAnswer() == userAnswer:
            correctQuestions.append(question)
        else:
            incorrectQuestions.append(question)
    questionList.setCorrectQuestion(correctQuestions)
    questionList.setIncorrectQuestion(incorrectQuestions)
    return render_template('answers.html', answers=questionList)

if __name__ == "__main__":
    app.run()
    