from flask import Flask, render_template, request
import datetime
import requests
import smtplib
import os
from dotenv import load_dotenv
#from post import Post

#get the year for the footer
current_year = datetime.datetime.now().year

# get email environment variables
load_dotenv()
MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWORD = os.getenv('MY_PASSWORD') #had to setup app passwords in gmail to get it to work

# get the posts from json bucket
posts = requests.get("https://api.npoint.io/d57a1ee2ce5110e0242c").json()


app = Flask(__name__)


# in index we link to the blog and are able to get a key, num passed in

@app.route('/')
def index_page():
    return render_template("index.html", year=current_year, all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=current_year)



@app.route('/about')
def about_page():
    return render_template("about.html", year=current_year)

@app.route('/contact', methods=["POST", "GET"])
def contact_page():

    if request.method == "POST":
        error = None
        
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        # email form submission info
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f'Subject:Monday Motivation\n\n Name: {data["name"]}\n Email: {data["email"]}/n Phone: {data["phone"]}/n Message: {data["message"]}')

        
        return render_template("contact.html", success_message=True, year=current_year)
    return render_template("contact.html", success_message=False, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)


