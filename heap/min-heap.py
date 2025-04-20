# What is a Heap?
# A Heap is a special tree-based data structure where:

# Min-Heap: The parent node is always smaller than or equal to its children. (Smallest element at the root)

# Insertion: O(log n) because we need to maintain the heap property after inserting a new element.

# Deletion (heappop): O(log n) because we need to maintain the heap property after removing the root element.
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

# Function | Description | Time Complexity
# heapq.heappush(heap, item) | Add item and maintain heap invariant | O(log n)
# heapq.heappop(heap) | Pop and return the smallest item | O(log n)
# heapq.heapify(lst) | Transform a list into a heap | O(n)
# heapq.heappushpop(heap, item) | Push then pop smallest (faster than separate ops) | O(log n)
# heapq.nlargest(n, iterable) | Return n largest elements | O(n log k)
# heapq.nsmallest(n, iterable) | Return n smallest elements | O(n log k)