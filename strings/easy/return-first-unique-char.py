# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.

def firstUniquechar(s):
    char_count = {}
    for i in s:
        char_count[i] = char_count.get(i, 0) + 1
    for i in s:
        if char_count[i] == 1:
            return s.index(i)
    return -1
# Time: O(n) — Looping over all characters
# Space: O(n) — Dictionary to store character counts
    print(char_count)


    
print(firstUniquechar("lleetcode"))