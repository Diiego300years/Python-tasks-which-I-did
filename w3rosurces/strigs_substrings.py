import unittest
"""Write a Python program to check the nth-1 string is a proper substring 
 of nth string in a given list of strings. 
"""

def substring(x: list):
    #basicly it's look easy when is in one line, but before I wrote it in 4, just now cut the lines  :)
    return x[-2] in x[-1]

class testStrings(unittest.TestCase):

    def testNo1(self):
        self.assertEqual(substring(['a', 'abb', 'sfs', 'oo', 'de', 'sfde']), True)

    def testNo2(self):
        self.assertEqual(substring(['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']), False)

    def testNo3(self):
        self.assertEqual(substring(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']), False)

    def testNo4(self):
        self.assertEqual(substring(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']), True)

if __name__ == '__main__':
    unittest.main()