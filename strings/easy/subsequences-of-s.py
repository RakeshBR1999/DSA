# Given a string s and a list of strings n, the task is to find all the subsequences of s that are present in n.
# return the subsequences of s that are present in n.
from itertools import combinations

def find_valid_subsequences(s: str, n: list[str]) -> list[str]:
    subsequences = set()
    length = len(s)
    
    # Generate all non-empty subsequences of s
    for i in range(1, length + 1):
        for combo in combinations(s, i):
            subsequences.add(''.join(combo))

    # Filter based on presence in list n
    n_set = set(n)  # To speed up lookup
    result = [sub for sub in subsequences if sub in n_set]
    
    return result

    
s = "rakesh"
n = ["ra","kes", "esh", "rakesh","ert"]
print(find_valid_subsequences(s,n))
# Output: ['ra', 'kes', 'esh', 'rakesh']

# Time: O(2^n) — Generating all subsequences
# Space: O(2^n) — Storing all subsequences
