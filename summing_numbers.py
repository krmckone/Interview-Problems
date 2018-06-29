import unittest

def are_equal(x, y):
    return x == y or x is y

def sum_to_k(x, y, k):
    return are_equal(x + y, k)

def sum_to_k_in_list(list, k):
    for index, number in enumerate(list):
        for number_other in list[index:]:
            if sum_to_k(number, number_other, k):
                return True
    return False
