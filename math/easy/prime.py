# return the total number of Prime Number in the N
def prime(num):
    if num < 2:
        return False
    # why we divide num by 2 +1
    # because if num is even then we can check only half of the numbers
    # if num is odd then we can check all the numbers
    # because odd numbers are not divisible by 2
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

def countPrimes(n):
    count = 0
    for i in range(2, n):
        if prime(i):
            count += 1
    return count

# Example usage:
n = 10
print(countPrimes(n))  # Output: 4

# it's giv
# Time: O(n) — Looping through the numbers
# Space: O(1) — No additional space used