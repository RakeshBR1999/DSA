# Creating a hash map
hash_map = {}

# Inserting key-value pairs
hash_map["apple"] = 100
hash_map["banana"] = 60
hash_map["orange"] = 80

# Accessing values
print(hash_map["apple"])    # Output: 100

# Updating a value
hash_map["apple"] = 120

# Checking existence
if "banana" in hash_map:
    print("Banana exists")

# Iterating
for fruit, price in hash_map.items():
    print(f"{fruit}: {price}")
