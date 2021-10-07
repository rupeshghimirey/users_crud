from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

# ==============================================
# Show Home Route that redirects to showAllUser
# ==============================================
@app.route("/")
def index():
    # call the get all classmethod to get all users
    return redirect('/showAllUser')

# ==========================================
# Route that shows the createUser.html page
# contains form for adding new user
# ==========================================
@app.route("/add_user")
def add_user_page():
    # call the get all classmethod to get all users
    return render_template("createUser.html")

# =====================================================
# This route shows when you submit the FORM
# routes on form matches the route here i.e create_user
# =====================================================
@app.route('/create_user', methods=["POST"])
def create_User():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "firstName": request.form["firstName"],
        "lastName" : request.form["lastName"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    id = User.save(data)
    path = "users" + "/" + str(id)
    print(id)
    # Don't forget to redirect after saving to the database.
    return redirect(path)


# =================================================
# Route for showing all users in the data base
# returning the page that which has listOfAllUsers
# =================================================
@app.route("/showAllUser")
def showAll():
    # call the get all classmethod to get all users
    listOfAllUsers = User.get_all()    
    print(session)
    return render_template("readAll.html", allUsers = listOfAllUsers)

# ====================================================
# Route coming from the link(Show) that has dynamic id
# Shows the info details of each user 
# ====================================================
@app.route("/users/<int:id>")
def userInfo(id):
    # call the get all classmethod to get all users
    data = {
        "user_id" : id
    }
    #returns the list with one user object(dictionary)
    user_one = User.get_one_user(data);
    print(user_one.first_name)
    return render_template("user_info.html", user_one = user_one)

# ==========================================================
# Route coming from the link(Delete) that has dynamic id
# Deletes the user and redirect to main menu i.e showAllUser 
# ==========================================================

@app.route("/users/<int:id>/delete")
def deleteUser(id):
    # call the get all classmethod to get all users
    data = {
        "user_id" : id
    }
    User.delete_user(data);
    return redirect("/showAllUser")

# ==============================================================
# Route coming from the link(Edit) that has dynamic id
# selected_user is passed so that we can grad the id in the page 
# ==============================================================
@app.route("/users/<int:id>/edit")
def edit_user(id):
    data = {
        "user_id" : id
    }
    selected_user = User.get_one_user(data);
    print(selected_user.first_name)

    return render_template("edit_user.html", selected_user = selected_user)

# ======================================================================
# routes coming from the FORM from the edit_user.html which matches the
#  <int:id> is passed dynamically from the FORM through jinga, so that data
# object can use that and later can be passed to the Query i.e UPDATE 
# ======================================================================
@app.route('/users/<int:id>/edit_user', methods=["POST"])
def get_edit_info(id):
    data = {
        "id": id,
        "firstName": request.form["firstName"],
        "lastName" : request.form["lastName"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.edit(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/showAllUser')
