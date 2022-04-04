import unittest
"""Write a Python program to check a given list of integers where the sum of the first i integers is i.
"""

def check(x: list):
    #it was pretty easy. Funcion returns True if value of lenght and sum of list is equal
    return len(x) == sum(x)


class testCheck(unittest.TestCase):

    def testNo1(self):
        self.assertEqual(check([0, 1, 2, 3, 4, 5]), False)

    def testNo2(self):
        self.assertEqual(check([1, 1, 1, 1, 1, 1]), True)


    def testNo3(self):
        self.assertEqual(check([2, 2, 2, 2, 2]), False)

if __name__ == '__main__':
    unittest.main()