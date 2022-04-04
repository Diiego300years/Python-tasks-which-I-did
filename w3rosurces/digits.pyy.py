# Write a Python program to find list integers containing exactly four distinct values,
# such that no integer repeats twice consecutively among the first twenty entries.

#
# Output:
# False
# Input:
#
import unittest


def digits(x: list):
    for i in range(len(x)-1):
        if x[i] != x[i + 1] and len(set(x)) == 4:
            return True
    return False


class testDigitsFunction(unittest.TestCase):

    def testNo1(self):
        self.assertEqual(digits([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]), True)

    def testNo2(self):
        self.assertEqual(digits([1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]), False)

    def testNo3(self):
        self.assertEqual(digits([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]), False)

if __name__ == '__main__':
    unittest.main()