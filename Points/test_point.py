import unittest
import point

class TopCharsTest(unittest.TestCase):
    
    def test_case_1st_quadrant(self):
        pnt = point.POINT(1,1)
        result = point.quadrant(pnt) 
        expected = 1
        self.assertEqual(result,expected)

    def test_case_2st_quadrant(self):
        pnt = point.POINT(-1,1)
        result = point.quadrant(pnt) 
        expected = 2
        self.assertEqual(result,expected)

    def test_case_3st_quadrant(self):
        pnt = point.POINT(-1,-1)
        result = point.quadrant(pnt) 
        expected = 3
        self.assertEqual(result,expected)

    def test_case_4st_quadrant(self):
        pnt = point.POINT(1,-1)
        result = point.quadrant(pnt) 
        expected = 4
        self.assertEqual(result,expected)

    def test_case_on_axis(self):
        pnt = point.POINT(0,0)
        result = point.quadrant(pnt) 
        expected = "point falls on axis."
        self.assertEqual(result,expected)



if __name__ == "__main__":
    unittest.main()