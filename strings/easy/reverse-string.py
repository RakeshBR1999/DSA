# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString(s):
        left, right = 0, len(s) - 1
        while left <right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        return s

# Example usage:
s = ["h","e","l","l","o"]
print(reverseString(s)) 
# Time: O(n) — Looping over all characters
# Space: O(1) — In-place swap

# second method
