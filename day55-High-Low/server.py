from flask import Flask
import random

app = Flask(__name__)


number = random.randint(0,9)

@app.route("/")
def home():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>"

@app.route("/<int:guess>")
def random_number(guess):
    if guess < number:
        return "<h1 style='text-align: center'>Too low, try again</h1>"
    elif guess > number:
        return "<h1 style='text-align: center'>Too high, try again</h1>"
    else:
        return "<h1 style='text-align: center'>You found me!</h1>"
    

if __name__ == "__main__":
    app.run(debug=True)