from user_profile import view_profile, update_profile, find_matches
from data import generate_random_profiles

# this is a simple User class for the demo
class User:
    # this class is for creating a user with their details like name, major, etc.
    def __init__(self, name, major, courses, study_habits, availability):
        # setting up the user's info when we make them
        self.name= name
        self.major =major
        self.courses = courses
        self.study_habits = study_habits
        self.availability= availability

    def add_course(self, course):
        # lets the user add a new course to their list
        self.courses.append(course)

    def update_availability(self, availability):
        # updates when the user is free to study
        self.availability = availability

# starting with no user logged in
demo_user = None

# generating some random profiles for matching
random_profiles = generate_random_profiles()

# welcome message for the app
print("Hello! Welcome to StudyBuddy - UMD College Park!")
print("We are so happy that you selected StudyBuddy to help you today!")
print("We will help you find your perfect study partners. Please enter your information to get started!!")

# main loop for the demo
while True:
    print("\n--- StudyBuddy - UMD College Park ---")
    if demo_user is None:
        # if no user is logged in, show the option to create an account
        print("1. Create Account")
    else:
        # if a user is logged in, show all the options
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Find Your Match")
        print("4. View Other Profiles")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if demo_user is None and choice == "1":
        # creating a new account
        name= input("Enter your name: ")
        major = input("Enter your major: ")
        courses=input("Enter your courses (comma-separated): ").split(",")
        study_habits =input("Enter your study habits: ")
        availability= input("Enter your availability: ")
        demo_user = User(name, major, courses, study_habits, availability)
        print("Account created successfully!")
    elif demo_user is not None and choice== "1":
        # viewing the user's profile
        view_profile(demo_user)
    elif demo_user is not None and choice== "2":
        # updating the user's profile
        update_profile(demo_user)
    elif demo_user is not None and choice == "3":
        # finding matches for the user
        print("\nAre you ready to find your match?")
        matches = find_matches(demo_user, random_profiles)
        if matches:
            print("\n--- Your Matches ---")
            for i, (match, score) in enumerate(matches, start=1):
                print(f"Match {i}:")
                print("Name:", match["name"])
                print("Major:", match["major"])
                print("Study Habits:", match["study_habits"])
                print("Availability:", match["availability"])
                print("Courses:", ", ".join(match["courses"]))
                print("-----------------------")
        else:
            print("Oops, no matches found.")
    elif demo_user is not None and choice == "4":
        # showing all the other profiles
        print("\n--- Other Profiles ---")
        for profile in random_profiles:
            print("Name:", profile["name"])
            print("Major:", profile["major"])
            print("Study Habits:", profile["study_habits"])
            print("Availability:", profile["availability"])
            print("Courses:", ", ".join(profile["courses"]))
            print("-----------------------")
    elif choice== "5":
        # exiting the app
        print("Thank you for using StudyBuddy. Goodbye!")
        break
    else:
        # handling invalid input
        print("Invalid choice. Please try again.")
