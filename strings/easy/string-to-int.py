# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
def myAtoi(s):
    s = s.strip()  # Remove leading and trailing whitespace
    if not s:
        return 0

    sign = 1
    index = 0
    n = len(s)

    # Check for sign
    if s[index] == '-':
        sign = -1
        index += 1
    elif s[index] == '+':
        index += 1

    result = 0

    # Convert characters to integer
    while index < n and s[index].isdigit():
        digit = int(s[index])
        result = result * 10 + digit
        index += 1

    result *= sign

    # Clamp the result to the 32-bit signed integer range
    if result < -2**31:
        return -2**31
    if result > 2**31 - 1:
        return 2**31 - 1

    return result
# Example usage:
s = "   -42"
print(myAtoi(s))  # Output: -42
s = "4193 with words"
print(myAtoi(s))  # Output: 4193
s = "words and 987"
print(myAtoi(s))  # Output: 0
s = "-91283472332"  

# Time: O(n) — Looping over the string
# Space: O(1) — Constant space for variables