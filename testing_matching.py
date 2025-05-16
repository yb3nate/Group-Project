import unittest
from user import User
from matching_logic import find_matches

class TestMatchingLogic( unittest.TestCase ):
# tests the find_matches function
# ensures that this function correctly identifies study buddies
    def test_find_matches( self ):
    # tests that the function successfully identifies a match based onoverlapping courses and same avaliability
    # creates at test using test functions
        user1 = User("Alice", "Computer Science", ["CS101", "Math101"], "Afternoons", "MWF 2-4pm")
        user2 = User( "Bob" , "Engineering" , ["CS101", "Physics101"] , "Afternoons" , "MWF 2-4pm")
        # Alice and Bob both have CS101 in common and their avaliability is the same
        # Bob should be returned in the matches for Alice

        all_users = [ user1 , user2 ]
    # verifies that only Bob is matched with Alice
    # asserts that only one match is found 
        matches = find_matches( user1 , all_users )
        self.assertEqual( len(matches) , 1 )   
        self.assertIn( user2 , matches )

if __name__ == "__main__":
     unittest.main()
