
from flask import Flask
import random
random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Guess the number between 0 and 9! </h2>"\
               "<img src='https://media.giphy.com/media/l0ExiSoCkhCfSm94k/giphy.gif'>"

@app.route("/<int:guess>")
def guess_no(guess):
    if guess >random_number:
        return  "<h2 style ='color:purple' > You guesses too high </h2>" \
                "<img src ='ttps://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif guess<random_number:
        return "<h2 style ='color:blue' > You guesses too low </h2>" \
               "<img src ='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h2 style ='color:red' > You got me </h2>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"



if __name__ == "__main__":
    app.run(debug=True)