'''
Input: a List of integers
Returns: a List of integers
'''

# Sample input: [0, 3, 1, 0, -2]
# Expected output: 3
# Expected output array state: [3, 1, -2, 0, 0]

# find 0s and indexes
# move 0 to right
# if no 0, keep the same value


def moving_zeroes(arr):
    # Your code here
    left = []
    right = []
    for i in range(len(arr)):
        if arr[i] != 0:
            left.append(arr[i])
            # print(arr[i])
        else:
            right.append(arr[i])
            # print(arr[i])
    left.extend(right)
    # print(y)
    return left


print(moving_zeroes([4, 2, 1, 5]))

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")