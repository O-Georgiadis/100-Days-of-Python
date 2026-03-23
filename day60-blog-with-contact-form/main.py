from flask import Flask, render_template, request
import requests
import os
import smtplib


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS_DAY47")
EMAIL_ADDRESS= os.getenv("EMAIL_ADDRESS_DAY47")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD_DAY47")

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html")

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, email_message)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
