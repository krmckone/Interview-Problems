# Author: Kaleb Robert McKone
# Date: 6/28/2018
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


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
