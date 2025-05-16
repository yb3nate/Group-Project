from user import User
from matching_logic import find_matches

def main():
    
    # runs the StudyBuddy app by creating a few fake users and trying to match them 
    # based on shared classes and when they’re free
    #
    # it’s just a sample to show what matching would look like in real life.
    
    user1 = User("Alice", "Computer Science", ["CS101", "Math101"], "Afternoons", "MWF 2-4pm")
    user2 = User("Bob", "Engineering", ["CS101", "Physics101"], "Afternoons", "MWF 2-4pm")

    all_users = [user1, user2]
    matches = find_matches(user1, all_users)
    
    for match in matches:
        print(match)

if __name__ == "__main__":
    main()
