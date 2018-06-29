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
