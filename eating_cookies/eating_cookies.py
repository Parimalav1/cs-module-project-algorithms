'''
Input: an integer
Returns: an integer
'''

def eating_cookies_v1(n):
    # print(n)
    # Your code here
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return eating_cookies_v1(n-1) + eating_cookies_v1(n-2) + eating_cookies_v1(n-3)

def eating_cookies_v2(n):
    # print(n)
    # Your code here
    if n < 0:
        return 0
    elif n == 0:
        return 1
    
    return eating_cookies_v2(n-1) + eating_cookies_v2(n-2) + eating_cookies_v2(n-3)

# print('eating_cookies_v1(5)', eating_cookies_v1(5))
# print('eating_cookies_v2(5)', eating_cookies_v2(5))
# e(1) = e(0) + e(-1) + e(-2)
# e(2) = e(1) + e(0) + e(-1) = 2
# e(3) = e(2) + e(1) + e(0) = 4
# e(4) = e(3) + e(2) + e(1) = 4 + 2 + 1
# 1111, 112, 121, 112, 22, 13, 31

# e(5) = e(4) + e(3) + e(2)
#     = ( e(3) + e(2) + e(1) ) +

def eating_cookies(n, cache=None):
    # print(n)
    # Your code here
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i: 0 for i in range(n + 1)}
            cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


# Runtime complexilty
# O(3^n)
# with caching/memoization, it is O(n)-linear