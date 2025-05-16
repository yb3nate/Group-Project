import unittest
from data import generate_random_profiles 

class TestData(unittest.TestCase):
    # testing the generate_random_profiles function
    # these tests check that the function returns the correct number of profiles
    # and that each profile has the required pieces of information
    def test_generate_profile_count(self):
        # makes sure the function actually generates the right number of profiles that we ask for
        # here we are testing for 3 profiles and then we check if we actually get 3 back
        profiles = generate_random_profiles(3)
        self.assertEqual(len(profiles), 3)  # should generate 3 profiles

    def test_profile_structure(self):
        # check that each genreated profile has the correct number of fields
        # here we are asking for asking for 1 profile and then has inside of it; name, major, study_habits, availability, courses
        # this basically helps us know that the function is working correctly and profiles are correctly structured
        profiles = generate_random_profiles(1)
        profile = profiles[0]
        self.assertIn("name", profile)
        self.assertIn("major", profile)
        self.assertIn("study_habits", profile)
        self.assertIn("availability", profile)
        self.assertIn("courses", profile)

if __name__ == "__main__":
    unittest.main()
