from user import User
from database import add_user, get_all_users
from matching_logic import find_matches
from profile import update_profile, view_profile

# This allows thefunction to create a new user and adds them to the database that is already existed.
def create_user(name, major, courses, study_habits, availability):
    new_user = User(name, major, courses, study_habits, availability)
    add_user(new_user)
    return f"User {name} created successfully."

# This shows all of the user's profile and what it entails.
def get_user_profile(name):
    user = next((u for u in get_all_users() if u.name == name), None)
    if user:
        return str(user)
    else:
        return "User not found."

#If any changes are made, this updates the user's profile
def update_user_profile(name, courses=None, study_habits=None, availability=None):
    user = next((u for u in get_all_users() if u.name == name), None)
    if user:
        update_profile(user, courses, study_habits, availability)
        return "Profile updated."
    else:
        return "User not found."
#This shows the users that are being paired together.
def find_user_matches(name):
    user = next((u for u in get_all_users() if u.name == name), None)
    if user:
        matches = find_matches(user, get_all_users())
        return [str(match) for match in matches]
    else:
        return "User not found."
