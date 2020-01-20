import unittest
import fuel_calculator

class TestAdventOfCode(unittest.TestCase):
    def test_calculateFuel(self):
        result = fuel_calculator.calculateFuel([6,9,12])
        self.assertEqual(result,3)

if __name__ == "__main__":
    unittest.main()