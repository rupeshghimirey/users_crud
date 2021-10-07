# import the function that will return an instance of a connection
from werkzeug.utils import redirect
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# ==========================================================
# GET METHOD, method that returns the list of the users
# ==========================================================
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users

# ==========================================================
# INSERT METHOD, method that returns id of the INSERTED user
# ***** Very Important*********
# ==========================================================
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) VALUES(%(firstName)s, %(lastName)s, %(email)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data )


# ==========================================================
# UPDATE METHOD, method that UPDATE the user object
# RETURNS NOTHING
# ***** Very Important*********
# ==========================================================
    @classmethod
    def edit(cls, data ):
        query = "UPDATE users SET first_name = %(firstName)s, last_name = %(lastName)s, email = %(email)s WHERE id = %(id)s"
        # data is a dictionary that will be passed into the edit method from server.py
        connectToMySQL('users').query_db( query, data )
# ==========================================================
# GET METHOD, method that returns the single object which is
# inside the list, index 0  i.e return (cls(result[0]));
# ***** Very Important*********
# ==========================================================
    @classmethod
    def get_one_user(cls, data ):
        query = "SELECT * FROM users WHERE id = %(user_id)s"
        result = connectToMySQL('users').query_db( query, data);
        return (cls(result[0]));

# ==========================================================
# DELETE METHOD, method that DELETE the user object based 
# dynamic id, RETURNS NOTHING
# ***** Very Important*********
# ==========================================================    

    @classmethod
    def delete_user(cls, data ):
        query = "DELETE FROM users WHERE id = %(user_id)s"
        connectToMySQL('users').query_db( query, data)

