import unittest
from threedigit import sum_is_ten, product_is_20, divisible_by_7, convert_xyz_to_int

class Tests(unittest.TestCase):

    def test0(self):
        self.assertTrue(sum_is_ten(0,9,1))
    
    def test1(self):
        self.assertTrue(sum_is_ten(1,8,1))
    
    def test2(self):
        self.assertTrue(sum_is_ten(5,4,1))
    
    def test3(self):
        self.assertTrue(sum_is_ten(2,2,6))
    
    def test4(self):
        self.assertFalse(sum_is_ten(0,0,0))
    
    def test5(self):
        self.assertFalse(sum_is_ten(10284,492,0))
    
    def test6(self):
        self.assertFalse(sum_is_ten(1,5,3))
    
    def test7(self):
        self.assertFalse(product_is_20(0,0,0))
    
    def test8(self):
        self.assertFalse(product_is_20(1,3,4))
    
    def test9(self):
        self.assertTrue(product_is_20(1,4,5))
    
    def test10(self):
        self.assertTrue(product_is_20(2,10,1))
    
    def test11(self):
        self.assertTrue(divisible_by_7(0,0,7))
    
    def test12(self):
        self.assertFalse(divisible_by_7(1,5,8098))
    
    def test13(self):
        self.assertEquals(convert_xyz_to_int(1,2,3), 123)
