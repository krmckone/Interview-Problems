import unittest
from summing_numbers import are_equal, sum_to_k, sum_to_k_in_list

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(are_equal(1, 1))
    
    def test_2(self):
        self.assertFalse(are_equal(1, 2))
    
    def test_3(self):
        self.assertTrue(sum_to_k(2, 3, 5))
    
    def test_4(self):
        self.assertFalse(sum_to_k(1, 2, 4))

    def test_5(self):
        self.assertFalse(sum_to_k_in_list([], 5))
    
    def test_6(self):
        self.assertTrue(sum_to_k_in_list([1,2], 3))
    
    def test_7(self):
        self.assertTrue(sum_to_k_in_list([1,3,5,6,7], 13))

    def test_8(self):
        self.assertTrue(sum_to_k_in_list([5,2,3,8,3],6))
    
    def test_9(self):
        self.assertFalse(sum_to_k_in_list([1,3,4,5,1,3,5],205))
    
    def test_10(self):
        self.assertFalse(sum_to_k_in_list([1,3,5,2,5], 1000))