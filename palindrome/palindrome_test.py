import palindrome
import unittest


class MyTest(unittest.TestCase):
    
    def test_palindrome(self):
        self.assertEqual(palindrome.word_checker('ABOBA'), True)

    def test_not_palindrome(self):
        self.assertEqual(palindrome.word_checker('Glory to Ukraine'), False)

if __name__ == '__main__':
    unittest.main()