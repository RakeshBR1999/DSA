arr = [1, 2, 2, 3, 1, 4]

freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)  # Output: {1: 2, 2: 2, 3: 1, 4: 1}
