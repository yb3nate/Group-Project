# This file is used to store users and retrieve them within the file

# This list all the user within
users_db = []  

def add_user(user):
    users_db.append(user)

def get_all_users():
    return users_db
