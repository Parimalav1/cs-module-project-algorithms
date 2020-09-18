'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


Sample input: [2, 2, 1]
Expected output: 1
```

```
Sample iput: [4, 1, 2, 1, 2]
Expected output: 4


def single_number(arr):
    # Your code
    arr.sort()
    for i in range(len(arr)):
        if i == 0:
            before = None
        else:
            before = arr[i-1]
        if i == len(arr) - 1:
            after = None
        else:
            after = arr[i+1]
        
        if arr[i] != before and arr[i] != after:  # [1,1,2,2,3]
            return arr[i]


print(single_number([1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]))


def single_number2(arr):
    for num in arr:  # O(n)
        if arr.count(num) == 1:  # 0(n) = O(n ** 2)
            return num


print(single_number2([1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]))


def single_number5(arr):
    # Your code here
    for i in range(0, len(arr)):  # O(n)
        if arr.count(arr[i]) == 1:  # O(n) = O(n ** 2)
            return arr[i]
    else:
        return None


print(single_number5([1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]))


def single_number3(arr):
    s = set()
    for num in arr:  # O(n) because the data is a set
        if num in s:  # O(1)
            s.remove(num)  # O(1)
        else:
            s.add(num)  # O(1)

    return list(s)[0]  # O(1)  = # O(n)


print(single_number3([1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]))


def single_number4(arr):
    # Your code
    nums = []
    for i in arr:  # O(n) because the data is a list
        if i in nums:  # O(n)  = O(n ** 2)
            nums.remove(i)
        else:
            nums.append(i)
    return nums.pop()


print(single_number4([1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]))
            
# input: array of numbers where there is one number that 
# is not a duplicate; every other number has a duplicate 
# O(n^2)
#def single_number(arr):
#    for num in arr: # O(n)
#        if arr.count(num) == 1: # O(n)
#            return num
#

# O(n)
def single_number(arr):
    # sets are a closely-related cousin to dicts 
    # they don't associate values with keys 
    # they're useful for when you need the uniqueness
    # property of dicts
    s = set()
    # s = []

    for num in arr: # O(n)
        if num in s: # O(1)
            s.remove(num) # O(1)
        else:
            s.add(num) # O(1)

    # at this point, the only element in the set 
    # is our odd-element-out
#    return list(s)[0] # O(1)
    return s.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")