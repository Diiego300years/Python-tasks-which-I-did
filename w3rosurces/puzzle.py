import unittest

""". Write a Python program find a list of integers with exactly two occurrences of nineteen
and at least three occurrences of five. Go to the editor
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True"""
def finding(x: list):
    #this function will return True or False
    #True - when is there a 2x 19 and 3x 5, False- else
    countingNineteen = 0
    countingFive = 0

    for i in x:
        if i == 19:
            countingNineteen += 1
        if i == 5:
            countingFive += 1

    if countingNineteen >= 2 and countingFive >= 3:
        return True
    return False


class TestSum(unittest.TestCase):

    def testingFinding(self):
        self.assertEqual(finding([19, 19, 15, 5, 3, 5, 5, 2]), True)

    def testing_finding(self):
        self.assertEqual(finding([19, 15, 15, 5, 3, 3, 5, 2]), False)

    def testingFindinG(self):
        self.assertEqual(finding([19, 19, 5, 5, 5, 5, 5]), True)

if __name__ == '__main__':
    unittest.main()