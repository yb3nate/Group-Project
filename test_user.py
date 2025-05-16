import unittest
from user import User

# unit test for the user class in relation to course management and avaliability updates
class TestUser(unittest.TestCase):
# tests the add_course method of the user class
# creates a user object with test data to ensure that the method correctly appends the new course to the list
# makes sure that there's nothing preventing the addition of another course
# assert function to ensure that the  new course was added to the user.courses
    def test_add_course(self):
        user= User("Alice", "Computer Science", ["CS101"], "Afternoons", "MWF 2-4pm")
        user.add_course("Math101")
        self.assertIn("Math101", user.courses)
# tests the update_avaliability method of the user class
# makes sure a users avaliability is properly updated when a change is made to the time
# creates a user object with test data and replaces the old avaliability with the new one
# asserts function used to confirm that the avalibility was changed 
    def test_update_availability(self):
        user = User("Alice", "Computer Science", ["CS101"], "Afternoons", "MWF 2-4pm")
        user.update_availability("Evenings")
        self.assertEqual(user.availability, "Evenings")

if __name__ == "__main__":
    unittest.main()
