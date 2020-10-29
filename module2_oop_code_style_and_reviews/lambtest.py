import unittest

from oop import COLORS, increment, SocialMediaUser
from random import randint

class SocialMediaUserTests(unittest.TestCase):
    """Tests for the usas of Social Media Users"""
    def setUp(self):
        self.user1 = SocialMediaUser(name='Jimmy', loc='France')
        self.user2 = SocialMediaUser(name='Peter', loc='England')
        self.user3 = SocialMediaUser(name='Nick', loc='Canada')

    def test_name(self):
        """Testing the name"""
        self.assertEqual(self.user1.name, 'Jimmy')
        self.assertEqual(self.user2.name, 'Peter')
    
    def test_location(self):
        """Testing the Location"""
        self.assertEqual(self.user1.loc, 'France')
        self.assertEqual(self.user2.loc, 'England')

    def test_defualt_upvotes(self):
        """Testing Upvotes"""
        self.assertEqual(self.user3.upvote, 0)

    def test_popular(self):
        """Testing the is popular method"""
        self.assertFalse(self.user3.is_popular())
        self.user3.recieve_upvote(randint(101, 10000))
        self.assertTrue(self.user3.is_popular())

class ExampleTests(unittest.TestCase):
    def test_inc(self):
        """Testing that increment adds 1 to a num"""
        x0 = 0
        y0 = increment(x0)
        self.assertEqual(y0, 1)

        x0 = 50
        y0 = increment(x0)
        self.assertEqual(y0, 51)

        x0 = -50
        y0 = increment(x0)
        self.assertEqual(y0, -49)
    
    def test_col(self):
        """Testing that a color is present in list"""
        self.assertIn('crimson', COLORS)
        self.assertNotIn('bannana', COLORS)
    
    def test_num_col(self):
        """Testing we have expected number of colors"""
        self.assertEqual(len(COLORS), 5)

if __name__ == "__main__":
    unittest.main()