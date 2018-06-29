import unittest

from list_products import new_array_product_of_originals_besides_i, multiply_list


class Tests(unittest.TestCase):

    def test_0(self):
        self.assertEquals(new_array_product_of_originals_besides_i([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
    
    def test_1(self):
        self.assertEquals(new_array_product_of_originals_besides_i([3, 2, 1]),[2, 3, 6])
    
    def test_2(self):
        self.assertEquals(new_array_product_of_originals_besides_i([0,0,0]), [0,0,0])
    
    def test_3(self):
        self.assertEquals(multiply_list([1,2,3]), 6)
    
    def test_4(self):
        self.assertEquals(multiply_list([3,4,10]), 120)
    
    def test_5(self):
        self.assertNotEquals(multiply_list([1,2,3,4]), 9023840)
    
    def test_6(self):
        self.assertEquals(multiply_list([0,0,0]), 0)
    
    def test_7(self):
        self.assertEquals(multiply_list([0,0,0,0,4,6,1,0]), 0)
    
    def test_8(self):
        self.assertEquals(new_array_product_of_originals_besides_i([1,2,2,3,3,4]),[144, 72, 72, 48, 48, 36])

    def test_9(self):
        self.assertNotEqual(new_array_product_of_originals_besides_i([1,1,1,1,1,1,4]), [5,5,5,5,5,5,5,5,])

    def test_10(self):
        self.assertNotEqual(new_array_product_of_originals_besides_i([1,19934,0,1,5,23231,14]), [5,45,5,5,0,5,25,5,])
    
    def test_11(self):
        self.assertEquals(new_array_product_of_originals_besides_i([1,1,1]), [1,1,1])
    
    def test_12(self):
        self.assertEquals(new_array_product_of_originals_besides_i([]), [])