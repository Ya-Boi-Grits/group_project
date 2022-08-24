# Where we define our routes!
from flask_app import app  # Needed for @app.route() among other things
from flask_app.models import user, strategy
# Import methods from Flask
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Routes for edit


@app.route('/new')
def new_cut_page():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    return render_template('edit_trade.html', this_user=user.User.get_user_by_id(data))
# route for registration


@app.route("/registration")
def registration():  # Root route that displays the login/registration page
    if "user_id" in session:
        return redirect('/dashboard')
    return render_template("registration.html")

# VISIBLE ROUTES


@app.route("/")
def index():  # Root route that displays the login/registration page
    if "user_id" in session:
        return redirect('/dashboard')
    return render_template("login_reg.html")


@app.route("/dashboard")
def dashboard():
    # IMPORTANT NOTE: If nobody is logged in, send them back to the login/register route
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session["user_id"]
    }
    return render_template("index.html", this_user=user.User.get_user_by_id(data), all_stategies=strategy.Strategy.get_strategies_by_user(data))


@app.route('/user/account')
def my_cuts_page():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }
    return render_template("update_user.html")

# INVISIBLE/HIDDEN ROUTES


# POST route where we register the user
@app.route("/register", methods=["POST"])
def register_user():
    print(request.form)
    # 1: Validate the form data to make sure everything is good
    if not user.User.validate_registration(request.form):
        # If it's no good, we send the user back
        return redirect("/registration")  # Send back to login/reg
    # If it's good, then we can register the user
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        # REMEMBER TO HASH YOUR PASSWORD!
        "password": bcrypt.generate_password_hash(request.form['password']),
    }
    # Save the user in the DB, then save the ID of the user in session
    session["user_id"] = user.User.register_user(data)
    # Redirect the user to the dashboard
    return redirect("/dashboard")


# POST route where we register the user
@app.route("/udpate_user", methods=["POST"])
def update_user():
    print(request.form)
    # 1: Validate the form data to make sure everything is good
    if not user.User.validate_registration_update(request.form):
        # If it's no good, we send the user back
        return redirect("/")  # Send back to login/reg
    # If it's good, then we can register the user
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": session["user_id"]
    }
    # Save the user in the DB, then save the ID of the user in session
    user.User.update_user(data)
    # Redirect the user to the dashboard
    return redirect("/dashboard")


@app.route("/login", methods=["POST"])  # POST route where we log in a user
def login_user():
    # Validation the login stuff
    found_user_or_false = user.User.validate_login(request.form)
    if found_user_or_false == False:
        # If it's no good, we send the user back
        return redirect("/")  # Send back to login/reg
    # Grab the user, then save the ID in session
    session["user_id"] = found_user_or_false.id
    # Send to the dashboard
    return redirect("/dashboard")


@app.route('/logout')
def logout():  # We need to clear session, then go to the login/reg page
    session.clear()
    return redirect("/")
