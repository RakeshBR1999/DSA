def quick_sort(data):
  if len(data) <= 1:
    return data

  pivot = data[-1]  # Choose last element as pivot
  left = [i for i in data[:-1] if i <= pivot]
  right = [i for i in data[:-1] if i > pivot]

  return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
data = [6, 5, 3, 1, 8, 7, 2, 4]
sorted_data = quick_sort(data)
print(sorted_data)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Time complexity: O(n log n) in average case, O(n^2) in worst case (when pivot selection is poor).

# Quick Sort:

# Advantages:

# Average-case time complexity of O(n log n), providing efficient sorting for most randomly distributed data.
# In-place sorting: Works on the original data array, reducing memory usage compared to Merge Sort.
# Can be highly efficient in practice with good pivot element selection, leading to faster sorting in many cases.

# Disadvantages:

# Worst-case time complexity of O(n^2) if the pivot element is always poorly chosen, 
# potentially significantly impacting performance for specific data distributions.
# Not stable sorting: May change the order of equal elements, which might be undesirable for certain applications.
# More complex to implement due to the need for efficient pivot selection and recursion handling.