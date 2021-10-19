import unittest

from water_overflow.main import *

class TestApp(unittest.TestCase):
    
    def test_hello_world(self):
        self.assertEqual(hello_world(), 'Hello world')

    def test_water_overflow(self):
        #  self.assertEqual(water_overflow(7, 1, 0), 1)
        #  self.assertEqual(water_overflow(15, 3, 2), 1)
        glasses = water_overflow(1)
        self.assertEqual(glasses[2][0].fill, 62.5)
        self.assertEqual(glasses[2][1].fill, 125)

    def test_glass(self):
        self.assertTrue(Glass(capacity=1, fill=1).isFull())
        self.assertFalse(Glass(capacity=250, fill=200).isFull())
        self.assertTrue(Glass(capacity=250, fill=300).isFull())

if __name__ == '__main__':
    unittest.main()
