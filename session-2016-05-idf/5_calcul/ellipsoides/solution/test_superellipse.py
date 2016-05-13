import unittest
import numpy.testing as npt

from superellipse import Superellipse


class TestAssert(unittest.TestCase):
     
    def setUp(self):
        se = Superellipse(1,1,2)
        self.x, self.y = se.cloud(5)
    
    def test_x(self):
        npt.assert_almost_equal(self.x, [1, 0, -1, 0, 1], decimal=7)
        
    def test_y(self):
        npt.assert_almost_equal(self.y, [0, 1, 0, -1, 0], decimal=7)


if __name__ == '__main__':
    unittest.main(verbosity=5) # par defaut verbosity=1
    
    
    