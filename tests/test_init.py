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

        glasses = water_overflow(3)
        self.assertEqual(glasses[4][3].fill, 171.875)
        self.assertEqual(glasses[3][0].fill, 156.25)

        glasses = water_overflow(5.2)
        last_row = glasses[len(glasses) - 1]
        have_water = False
        for glass in last_row:
            if glass.fill > 0:
                have_water = True
                break

        self.assertTrue(have_water)

    def test_glass(self):
        self.assertTrue(Glass(capacity=1, fill=1).isFull())
        self.assertFalse(Glass(capacity=250, fill=200).isFull())
        self.assertTrue(Glass(capacity=250, fill=300).isFull())

if __name__ == '__main__':
    unittest.main()
