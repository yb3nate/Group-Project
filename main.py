from user import User
from database import add_user, get_all_users
from matching_logic import find_matches
from profile import view_profile, update_profile

# This is where users can update their profiles for people to view and share
def main():
    print("Welcome to StudyBuddy!")

# This is example users and shows what it will look like 
    user1 = User("Alice", "Computer Science", ["CS101", "Math101"], "Afternoons", "MWF 2-4pm")
    user2 = User("Bob", "Engineering", ["CS101", "Physics101"], "Afternoons", "MWF 2-4pm")

# Add the users to the database
    add_user(user1)
    add_user(user2)

 # Main loop to display options to the user
    while True:
        print("\nMenu:")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Find Study Matches")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name to view profile: ")
            user = next((u for u in get_all_users() if u.name == name), None)
            if user:
                view_profile(user)
            else:
                print("User not found.")
        elif choice == "2":
            name = input("Enter your name to update profile: ")
            user = next((u for u in get_all_users() if u.name == name), None)
            if user:
                courses = input("Enter your new courses (comma-separated): ").split(", ")
                study_habits = input("Enter your new study habits: ")
                availability = input("Enter your new availability: ")
                update_profile(user, courses, study_habits, availability)
            else:
                print("User not found.")
        elif choice == "3":
            name = input("Enter your name to find study matches: ")
            user = next((u for u in get_all_users() if u.name == name), None)
            if user:
                matches = find_matches(user, get_all_users())
                if matches:
                    print("Your study matches are:")
                    for match in matches:
                        print(match)
                else:
                    print("No matches found.")
            else:
                print("User not found.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
