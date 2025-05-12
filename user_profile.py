# This file lets users view and update their profile information to be able to share with others
# People will be able to send information to share and pair up with one another

# This shows the user's basic profile info
def view_profile(user):
    print("------ User Profile ------")
    print("Name:", user.name)
    print("Major:", user.major)
    print("Courses:", ", ".join(user.courses))
    print("Study Habits:", user.study_habits)
    print("Availability:", user.availability)
    print("--------------------------")

# This lets the user update their profile details
def update_profile(user):
    print("What would you like to update?")
    print("1. Name")
    print("2. Major")
    print("3. Add a Course")
    print("4. Study Habits")
    print("5. Availability")
#Allows user to implement a number into code
    choice = input("Enter a number (1-5): ")

    if choice =="1":
        new_name= input("Enter your new name: ")
        user.name = new_name

    elif choice== "2":
        new_major = input("Enter your new major: ")
        user.major =new_major

    elif choice== "3":
        new_course = input("Enter the course to add: ")
        user.add_course(new_course)

    elif choice == "4":
        new_habits =input("Enter your new study habits: ")
        user.study_habits= new_habits

    elif choice == "5":
        new_avail =input("Enter your new availability: ")
        user.update_availability(new_avail)

    else:
        print("Invalid choice.")

