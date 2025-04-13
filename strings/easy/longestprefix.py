# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as the prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the array
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]  # Shorten the prefix
            if not prefix:
                return ""
    
    return prefix
# Example usage:
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))  # Output: "fl"
strs = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs))  # Output: ""

# Time: O(n * m) — n is the number of strings and m is the length of the longest string
# Space: O(1) — No extra space used
# The function iteratively reduces the prefix until it finds a common prefix or exhausts it.