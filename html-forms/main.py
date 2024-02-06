from flask import Flask, render_template, request
import datetime
#from post import Post

#get the year for the footer
current_year = datetime.datetime.now().year

app = Flask(__name__)


# in index we link to the blog and are able to get a key, num passed in

@app.route('/')
def index_page():
    return render_template("index.html", year=current_year)


@app.route('/login', methods=["POST"])
def receive_data():
    error = None

    name = request.form['username']
    password = request.form['userpass']
    return render_template('login.html', loginname = name, loginpass = password, error=error) 
    




if __name__ == "__main__":
    app.run(debug=True)




