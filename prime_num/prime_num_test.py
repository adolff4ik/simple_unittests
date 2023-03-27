import prime_num
import unittest


class MyTest(unittest.TestCase):
    
    def test_prime_num(self):
        self.assertEqual(prime_num.num_checker(4), False)
    
    def test_float(self):
        self.assertEqual(prime_num.num_checker(4.5), True)

    def test_str(self):
        self.assertEqual(prime_num.num_checker('Glory to Ukraine'), 'Enter num, please')

if __name__ == '__main__':
    unittest.main()