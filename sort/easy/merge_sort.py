# Array: [8, 4, 5, 3, 7, 2, 6, 1]
# Split: [8, 4, 5, 3] and [7, 2, 6, 1]
# Split again: [8, 4], [5, 3], [7, 2], [6, 1]
# Keep splitting until single elements: [8], [4], [5], [3], [7], [2], [6], [1]
# Merge pairs: [4, 8], [3, 5], [2, 7], [1, 6]
# Merge again: [3, 4, 5, 8], [1, 2, 6, 7]
# Final merge: [1, 2, 3, 4, 5, 6, 7, 8]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted or empty array
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare elements and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# Example usage
arr = [8, 4, 5, 3, 7, 2, 6, 1]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)


# Time Complexity: O(n log n)
# The time complexity of Merge Sort is O(n log n) in all cases (best, average, and worst).
 # Spcae Complexity: O(n)
# The space complexity of Merge Sort is O(n) due to the additional space required for merging.

#  O(n log n) in average and worst case.
# 
# Trade-offs between Merge Sort and Quick Sort:

# Both Merge Sort and Quick Sort are powerful sorting algorithms widely used for their efficiency,
#  but they each have distinct trade-offs to consider:

# Merge Sort:

# Advantages:

# Guaranteed O(n log n) time complexity in both average and worst cases, 
# ensuring consistent performance regardless of input data.
# Stable sorting algorithm: Preserves the original order of equal elements,
#  useful for maintaining specific ordering within the sorted data.
# Simple to implement and understand conceptually, making it a good choice for beginners.

# Disadvantages:

# Requires additional memory space equal to the size of the input data for merging sublists,
#  which can be a constraint for large datasets or limited memory environments.
# Not in-place sorting: Modifies the original data by creating copies for sublists,
#  potentially hindering performance in certain scenarios.

