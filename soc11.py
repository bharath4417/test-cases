def subtract(a, b):
    return a-b

import unittest

class subtractCase(unittest.TestCase):
    def test1(self):
        
        result = subtract(10,7)
        
        self.assertEqual(result, 3)
    
    def test2(self):
        
        result = subtract(-5,2)
        
        self.assertEqual(result, -7)

    def test3(self):
        
        result = subtract(19,-7)
        
        self.assertEqual(result, 26)

    def test4(self):
        
        result = subtract(-20,6)
        
        self.assertEqual(result, -26)

    def test5(self):
        
        result = subtract(2,2)
        
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
