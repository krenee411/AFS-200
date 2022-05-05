from flask import Flask, request, render_template

import triviaquestion 


from triviagame import TriviaGame 


app = Flask(__name__)

questionList = TriviaGame()
questionList.getData(3,20)
@app.route("/",methods=["GET"])
def home():
    return render_template('questionPage.html',results = questionList.getAllQuestions() )




if __name__ == "__main__":
    app.run()
    