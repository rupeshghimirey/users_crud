from flask import Flask, render_template, session, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)
app.secret_key = "random key for flask"  

@app.route("/")
def index():
    # call the get all classmethod to get all users
    return redirect('/showAllUser')

@app.route("/add_user")
def add_user_page():
    # call the get all classmethod to get all users
    return render_template("createUser.html")


# relevant code snippet from server.py
from user import User

#----------------------------------------
# Adding a New User
#----------------------------------------
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

@app.route("/showAllUser")
def showAll():
    # call the get all classmethod to get all users
    listOfAllUsers = User.get_all()    
    print(session)
    return render_template("readAll.html", allUsers = listOfAllUsers)

#----------------------------------------
# Show a User Info
#----------------------------------------
@app.route("/users/<int:id>")
def userInfo(id):
    # call the get all classmethod to get all users
    data = {
        "user_id" : id
    }
    user_one = User.get_one_user(data);
    print(user_one.first_name)
    return render_template("user_info.html", user_one = user_one)

@app.route("/users/<int:id>/delete")
def deleteUser(id):
    # call the get all classmethod to get all users
    data = {
        "user_id" : id
    }
    User.delete_user(data);
    return redirect("/showAllUser")


# templates for edit user
@app.route("/users/<int:id>/edit")
def edit_user(id):
    data = {
        "user_id" : id
    }
    selected_user = User.get_one_user(data);
    print(selected_user.first_name)

    return render_template("edit_user.html", selected_user = selected_user)

# route for sending edited information
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

if __name__ == "__main__":
    app.run(debug=True)