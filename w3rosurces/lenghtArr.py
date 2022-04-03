import unittest
"""Write a Python program that accept a list of integers and check the length and the fifth element.
Return true if the length of the list is 8 and fifth element occurs thrice in the said list.


Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True

Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False

Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True

Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False"""


def finding(x: list):
    return len(x) == 8 and x.count(x[4]) == 3


class TestLenght(unittest.TestCase):

    def testingFinding(self):
        self.assertEqual(finding([19, 19, 15, 5, 5, 5, 1, 2]), True)

    def testing_finding(self):
        self.assertEqual(finding([19, 15, 15, 5, 3, 3, 5, 2]), False)

    def testingFindinG(self):
        self.assertEqual(finding([11, 12, 14, 13, 14, 13, 15, 14]), True)

    def testingFindinG(self):
        self.assertEqual(finding([19, 15, 11, 7, 5, 6, 2]), False)

if __name__ == '__main__':
    unittest.main()
