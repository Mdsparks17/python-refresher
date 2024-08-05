import unittest

class MyFunctions:
    def __init__(self):
        pass

    def getNumberOfLetter(self, letter: str, text: str) -> int:
        count = 0
        for s in text:
            if s == letter:
                count += 1
        return count
    
    def getNumberOfLetterBad(self) -> int:
        return '42'

class MyTests(unittest.TestCase):
    def setUp(self):
        self.f = MyFunctions()

    def test_strict_typing(self):
        self.assertTrue(self.f.getNumberOfLetter('a', 'asdfjklasdfjkl'), 2)
        self.assertRaises(TypeError, self.f.getNumberOfLetter(2, 'asdfjklasdfjkl'), 2)
        self.assertRaises(TypeError, self.f.getNumberOfLetter(2, 'asdfjklasdfjkl'), 2)
        # Does not throw because return typing is not checked at runtime!
        self.assertRaises(TypeError, self.f.getNumberOfLetterBad())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

