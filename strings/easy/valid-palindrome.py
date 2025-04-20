# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
def isPalindrome(s):
    filtered_chars = []
    for char in s:
        if char.isalnum():
            filtered_chars.append(char.lower())
    left, right = 0, len(filtered_chars) - 1
    while left < right:
        if filtered_chars[left] != filtered_chars[right]:
            return False
        left += 1
        right -= 1
    return True

s = "rar"
print(isPalindrome(s))


# Time: O(n) — Looping over all characters
# Space: O(n) — List to store filtered characters