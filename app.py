from flask import Flask, request, session, render_template, redirect
app = Flask(__name__)
DB = {
    "users": {
        1: {"username": "MK", "password": "pass"}
    },
    "stores": {

    },
    "products": {

    }
}

@app.route("/")
def home():
    is_logged_in = 'username' in session
    if is_logged_in:
        return render_template('home_logged_in.html', title='Home', username=session["username"])
    else:
        return render_template('home_logged_out.html', title='Home', welcoming_message='Welcome to store')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # if POST, add user to database
        # redirect to login page
        userId = len(DB["users"].keys()) + 1
        DB["users"][userId] = {"username": request.form["username"], "password": request.form["password"]}
        return redirect("/login")
    else:
        # if GET, display signup page
        return render_template('signup.html', title='Sign Up')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # if POST, check if an existing user exists in the DB
        # if so, log them in i.e.
        session["username"] = request.form["username"]
        return redirect("/")
    else:
        # if GET, display login page
        return render_template('login.html', title='Sign Up')

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    del session["username"]
    return redirect("/")

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run(port=3000, debug=True)
