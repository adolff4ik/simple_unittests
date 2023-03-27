import str_to_list
import unittest


class MyTest(unittest.TestCase):
    
    def test_prime_num(self):
        self.assertEqual(str_to_list.str_to_list('Glory to Ukraine'), ['Glory', 'to', 'Ukraine'])
    
    def test_float(self):
        self.assertEqual(str_to_list.str_to_list(' Glory     to     Ukraine     '), ['Glory', 'to', 'Ukraine'])


if __name__ == '__main__':
    unittest.main()