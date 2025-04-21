import unittest
from user import User

class TestUser(unittest.TestCase):
#This sees if user would be allowed to add course
    def test_add_course(self):
        user= User("Alice", "Computer Science", ["CS101"], "Afternoons", "MWF 2-4pm")
        user.add_course("Math101")
        self.assertIn("Math101", user.courses)
#Shows and checks to see if the users availability is correctly up to date
    def test_update_availability(self):
        user = User("Alice", "Computer Science", ["CS101"], "Afternoons", "MWF 2-4pm")
        user.update_availability("Evenings")
        self.assertEqual(user.availability, "Evenings")

if __name__ == "__main__":
    unittest.main()