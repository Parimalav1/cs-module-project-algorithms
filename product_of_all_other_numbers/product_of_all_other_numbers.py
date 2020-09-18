'''
Input: a List of integers
Returns: a List of integers
'''

# For example, given
# ```
# [1, 7, 3, 4]
# ```
# your function should return
# ```
# [84, 12, 28, 21]
# ``` 
# by calculating
# ```
# [7*3*4, 1*3*4, 1*7*4, 1*7*3]


import functools


def product_of_all_other_numbers(arr):
    # Your code here
    # make an empty array
    # exclude the index or value
    # multiply nums
    # append it to array
    # new_arr = []
    
    newList = []
    for i in range(len(arr)):
        product = 1
        for x in range(len(arr)):
            product *= arr[x]
        product /= arr[i]
        newList.append(int(product))
    return newList


print(product_of_all_other_numbers([2,5,8,11]))

def product_of_all_other_numbers2(arr):
    newList = []
    for i in range(len(arr)):
        product = functools.reduce(lambda accum, curr: curr * accum, arr) / arr[i]
        newList.append(int(product))
    return newList


print(product_of_all_other_numbers2([2,5,8,11]))

# Has anyone figured out a way of multiplying all numbers in a list without using a loop? 
# Is it even possible?
# well you could chop the list up into segments of size 1, 
# multiply segments and pass the products up the stack recursively,
# remember the associative property: Any group of three or more numbers multiplied together will end in the same product no matter the grouping
# so: (a*b*c*d*e*f*g*h) = ((a*b) * (c*d)) * ((e*f) * (g* h))


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
