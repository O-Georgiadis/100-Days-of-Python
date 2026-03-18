from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=year)



@app.route("/guess/<name>")
def guess(name):
    name = name.title()
    GENDER_URL = f"https://api.genderize.io?name={name}"
    AGE_URL = f"https://api.agify.io?name={name}"

    gender_response= requests.get(GENDER_URL)
    gender = gender_response.json()["gender"]
    age_response = requests.get(AGE_URL)
    age = age_response.json()["age"]

    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)
    
if __name__ == "__main__":
    app.run(debug=True)