import unittest
import naturals

class TestAdventOfCode(unittest.TestCase):
    
    def test_calculateFuel(self):
        result = naturals.sum_naturals(7)
        self.assertEqual(result,28)

if __name__ == "__main__":
    unittest.main()