from flask import Flask, request, render_template

import triviaquestion 


from triviagame import TriviaGame 


app = Flask(__name__)

questionList = TriviaGame()
questionList.getData(3,20)

@app.route("/",methods=["GET"])
def home():
    return render_template('questionPage.html',questions=questionList.getAllQuestions() )


@app.route("/score", methods=['POST'])
def score():
    user_answer = request.form.get('1')
    return render_template('answers.html', answers=questionList.getAllQuestions(), userAnswer=user_answer)

if __name__ == "__main__":
    app.run()
    