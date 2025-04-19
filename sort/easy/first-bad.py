# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. Since each version is 
# developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        # why are we using this formula?
        # To prevent overflow in languages with fixed integer sizes
        # In Python, this is not a concern, but it's a good practice
        # to use this formula for binary search
        # to avoid overflow in other languages.
        # mid = (left + right) // 2
        # Using the formula to prevent overflow
        # mid = left + (right - left) // 2
        # This is equivalent to (left + right) // 2 but avoids overflow
        # mid = left + (right - left) // 2
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    # why are we returning left?
    # left will be the first bad version because when we exit the loop,
    # left will be the first version that is bad.
    # If left is not bad, then the first bad version is left + 1
    return left
# Example usage     
n = 5
def isBadVersion(version):
    # Simulating the API call
    return version >= 4  # Let's say version 4 and above are bad
print(firstBadVersion(n))  # Output: 4  