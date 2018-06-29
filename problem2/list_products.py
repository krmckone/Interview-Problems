# Author: Kaleb Robert McKone
# Date: 6/29/2018
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?
# I didn't use division

def multiply_list(in_list):
    product = in_list[0]
    for element in in_list[1:]:
        product *= element
    return product


# BUG: This does not work with lists that all contain the same elements. Example: [1,1,1,1] will always return [] 
# since the comprehension checks for equality and will throw that number out. All numbers are thrown out since all numbers
# in the list are equal to eachother. test_2 always fails in multiply_list since the empty list has no index 0 element.
def new_array_product_of_originals_besides_i(in_list):
    new_list = []
    for number in in_list:
        unique_list = [x for x in in_list if x != number]
        new_list.append(multiply_list(unique_list))
    return new_list

