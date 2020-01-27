import unittest
from bank_queue import BankQueue

class TestsQueue(unittest.TestCase):
    q = BankQueue()

    def test_pop(self):
        result = self.q.push(1)
        result = self.q.push(2)
        result = self.q.push(3)
        self.assertEqual(result,[1,2,3])
    def test_push(self):
        result = self.q.pop()
        self.assertEqual(result,[2,3])
    def test_clear(self):
        result = self.q.clear()
        self.assertEqual(result,[])
        

if __name__ == "__main__":
    unittest.main()