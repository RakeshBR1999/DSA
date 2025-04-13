# A digit string is good if the digits (0-indexed) at even indices are even and
# the digits at odd indices are prime (2, 3, 5, or 7).
# For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
# Input: n = 1
# Output: 5
# Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

def countGoodNumbers(n):
    even_digits = 5  # 0, 2, 4, 6, 8
    odd_digits = 4   # 2, 3, 5, 7
    mod = 10**9 + 7   # Large prime modulus to avoid overflow
    # A large prime number
    # Helps avoid collisions in modular arithmetic
    
    # If n is even, we divide positions equally:
        # Half even-digit positions
        # Half odd-digit positions
    if n % 2 == 0:
        return pow(even_digits, n // 2, mod) * pow(odd_digits, n // 2, mod) % mod
    else:
        # If n is odd, we assume:
            # One more even-position than odd
            # Because index starts from 0 (even)
        return pow(even_digits, n // 2 + 1, mod) * pow(odd_digits, n // 2, mod) % mod
    
    # pow(5, 2, mod) * pow(4, 1, mod) % mod
    # = 25 * 4 = 100 % mod
    # = 100

# Example usage:
n = 1
print(countGoodNumbers(n))  # Output: 5
n = 4
print(countGoodNumbers(n))  # Output: 400