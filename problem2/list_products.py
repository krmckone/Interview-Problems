# Author: Kaleb Robert McKone
# Date: 6/29/2018
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?
# I didn't use division in my intial solution. However, it's clear to see that one other solution is to get the product of all numbers in the list, then for each index,
# divide the product by the number at that index to get the result list.
# product = multiply_list(in_list)
# result_list = [product / number for number in in_list]

def multiply_list(in_list):
    if in_list:
        product = in_list[0]
        for element in in_list[1:]:
            product *= element
        return product
    else:
        return 0


def new_array_product_of_originals_besides_i(in_list):
    new_list = []
    for index,number in enumerate(in_list):
        unique_list = [other_number for other_index,other_number in enumerate(in_list) if (other_index,other_number) != (index,number)]
        new_list.append(multiply_list(unique_list))
    return new_list

