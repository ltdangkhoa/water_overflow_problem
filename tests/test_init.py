import unittest
from water_overflow.main import hello_world, water_overflow

class TestApp(unittest.TestCase):
    
    def test_hello_world(self):
        self.assertEqual(hello_world(), 'Hello world')

    def test_water_overflow(self):
        #  self.assertEqual(water_overflow(7, 1, 0), 250)
        #  self.assertEqual(water_overflow(15, 3, 2), 250)
        self.assertEqual(water_overflow(1, 2, 0), 62.5)
        self.assertEqual(water_overflow(1, 2, 1), 125)

if __name__ == '__main__':
    unittest.main()
