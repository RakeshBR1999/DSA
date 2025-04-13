# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
def isAnagram(st1, st2):
    if len(st1)!=len(st2):
        return False
    count = {}

    for i in st1:
        count[i] = count.get(i, 0) + 1
    for i in st2:
        if i not in count:
            return False
        count[i]-=1
        if count[i]<0:
            return False
    
    return True
# Example usage:
st1 = "anagram"
st2 = "nagaram"
print(isAnagram(st1, st2)) # True
st1 = "rat"
st2 = "car"
print(isAnagram(st1, st2)) # False


# Time: O(n) — Looping over all characters
# Space: O(n) — Dictionary to store character counts

