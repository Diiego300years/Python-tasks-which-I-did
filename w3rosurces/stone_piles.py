import unittest
"""We are making n stone piles! The first pile has n stones.
If n is even, then all piles have an even number of stones.
If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous
pile but as few as possible. Write a Python program to find the number of stones in each pile.
"""

def pile(x):
    arr = []
    if x % 2 == 0:
        for i in range(x):
            c = x + 2 * i
            arr.append(c)
        return arr
    if x % 2 != 0:
        for i in range(x):
            c = x + 2 * i
            arr.append(c)
        return arr


class TestBig(unittest.TestCase):

    def test_int(self):
        self.assertEqual(pile(2), [2,4])

    def test_no2(self):
        self.assertEqual(pile(10), [10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_no3(self):
        self.assertEqual(pile(3), [3, 5, 7])

    def test_no4(self):
        self.assertEqual(pile(17), [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])

if __name__ == '__main__':
    unittest.main()