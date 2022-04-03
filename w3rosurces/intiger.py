import unittest
"""Write a Python program that accept an integer test whether an integer greater
than 4^4 and which is 4 mod 34."""

def multiply(x):
    #this function return easy way intiger using modulo
    return x > (4**4) and x%34 == 4


class testIntiger(unittest.TestCase):

    def testingFinding(self):
        self.assertEqual(multiply(922), True)

    def testing_Finding(self):
        self.assertEqual(multiply(914), False)

    def testing__Finding(self):
        self.assertEqual(multiply(854), True)



if __name__ == '__main__':
    unittest.main()