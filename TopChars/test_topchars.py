import unittest
import topchars

class TopCharsTest(unittest.TestCase):
    
    def test_case(self):
        txt = 'AAAAAaaaaa BBBBbbbbb CCCCcccc DDDdddd EEEeee FFfff GGgg Hhh Ii J'
        result  = topchars.topchars.countchars(txt)
        expected = [('A',10),('B',9),('C',8),('D',7),('E',6),('F',5),('G',4),('H',3),('I',2),('J',1)]
        expected.reverse()
        self.assertEqual(result,expected)

if __name__ == "__main__":
    unittest.main()