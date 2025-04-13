# What is a Heap?
# A Heap is a special tree-based data structure where:

# Min-Heap: The parent node is always smaller than or equal to its children. (Smallest element at the root)
# Max-Heap: The parent node is always larger than or equal to its children. (Largest element at the root)

#  Insertion: O(log n)
# Deletion (heappop): O(log n)
# Accessing Min Element: O(1)

import heapq

# Create an empty heap
heap = []

# Insert elements into the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 8)
heapq.heappush(heap, 2)

print("Heap:", heap)  # Internally it maintains the heap property

# Extract the smallest element (root)
smallest = heapq.heappop(heap)
print("Smallest Element:", smallest)
print("Heap after removal:", heap)
