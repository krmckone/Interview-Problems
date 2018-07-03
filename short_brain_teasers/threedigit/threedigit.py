# Author: Kaleb Robert McKone
# Date: 7/3/2018

# This question is from the Daily Brew Newsletter.

# There's a 3-digit number. The sum of its digits is 10, 
# the product of its digits is 20, and it is divisible by 7. 
# What is the 3-digit number?

def sum_is_ten(x,y,z):
    return x + y + z == 10

def product_is_20(x,y,z):
    return x * y * z == 20

def divisible_by_7(x,y,z):
    num = convert_xyz_to_int(x,y,z)
    return num % 7 == 0

def convert_xyz_to_int(x,y,z):
    return int(str(x) + str(y) + str(z))

def find_three_digits():
    possible_digits = range(1,10)
    for x in possible_digits:
        for y in possible_digits:
            for z in possible_digits:
                if product_is_20(x,y,z) and sum_is_ten(x,y,z) and divisible_by_7(x,y,z):
                    return convert_xyz_to_int(x,y,z)


print(find_three_digits())

