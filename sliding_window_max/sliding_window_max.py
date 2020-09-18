'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Expected Output: [3,3,5,5,6,7] 
# Explanation: 


# Window position                Max
# ---------------               -----
# [1  3  2] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# new = []
# cur_idx = x
# i = 0
# i < len(arr)
# arr[x] > arr[i]
# i +=1 
# new.append(arr[x])


def sliding_window_max(nums, k):
    # Your code here
    new_arr = []
    if len(nums) < k:
        nums.sort()
        return [nums[-1]]
    for i in range((len(nums) - k) + 1):
        max = None
        for j in range(i, i + k]:
            if max == None:
                max = nums[j]
            else:
                if nums[j] > max:
                    max = nums[j]
        new_arr.append(max)

    return new_arr


print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))

def sliding_window_max2(nums, k):
    # Your code here
    new_arr = []
    if len(nums) < k:
        nums.sort()
        return [nums[-1]]
    i = 0
    # while i < (len(nums) - k) + 1:
    for i in range((len(nums) - k) + 1):
        max = None
        for j in range(i, i + k]:
            if max == None:
                max = nums[j]
            else:
                if nums[j] > max:
                    max = nums[j]
        new_arr.append(max)
        # i += 1
    return new_arr


print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
