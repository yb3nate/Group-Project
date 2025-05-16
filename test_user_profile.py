import unittest
from unittest.mock import patch
from user_profile import view_profile, update_profile
from user import User

class TestUserProfile(unittest.TestCase):
    # testing the view_profile function to ensure that the viewing and updating of profiles is functional
    # verifies that the profile informationis correctly printed when view_profile is called
    # tests the name update fuction in the update_profile function
    @patch("builtins.print")
    def test_view_profile(self, mock_print):
        # creates a sample user profile with test data
        # checks that print is called with the correct values
        user = User("Alice", "CS", ["CS101"], "Night owl", "Weekends")
        view_profile(user)
        # ensures that the rpint function is called with the expected values
        mock_print.assert_any_call("Name:", "Alice")
        mock_print.assert_any_call("Major:", "CS")

    # testing the update_profile function correctly updates the user's name
    @patch("builtins.input", side_effect=["1", "Bob"])
    def test_update_name(self, mock_input):
        # creates a sample user object with test data
        # calls the update_profile function to check if the name is updated
        user = User("Alice", "CS", ["CS101"], "Night owl", "Weekends")
        update_profile(user)
        # checks that the name is updated correctly
        self.assertEqual(user.name, "Bob")

if __name__ == "__main__":
    unittest.main()
