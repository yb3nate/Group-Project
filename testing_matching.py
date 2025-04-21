import unittest
from user import User
from matching_logic import find_matches

class TestMatchingLogic( unittest.TestCase ):

    # makes sure the match function actually finds study buddies
    # who have overlapping classes and times that work
    # in this case: Alice should match with Bob
    def test_find_matches( self ):
        user1 = User("Alice", "Computer Science", ["CS101", "Math101"], "Afternoons", "MWF 2-4pm")
        user2 = User( "Bob" , "Engineering" , ["CS101", "Physics101"] , "Afternoons" , "MWF 2-4pm")

        all_users = [ user1 , user2 ]

        matches = find_matches( user1 , all_users )
        self.assertEqual( len(matches) , 1 )    # just bob
        self.assertIn( user2 , matches )

if __name__ == "__main__":
     unittest.main()