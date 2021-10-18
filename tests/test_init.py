import unittest
from water_overflow.main import hello_world

class TestApp(unittest.TestCase):
    
    def test_hello_world(self):
        self.assertEqual(hello_world(), 'Hello world')


if __name__ == '__main__':
    unittest.main()
