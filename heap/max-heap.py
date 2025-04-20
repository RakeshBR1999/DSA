# Max-Heap: The parent node is always larger than or equal to its children. (Largest element at the root)
import heapq


# Create a max-heap by inverting the values
class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        # Invert the value to use min-heap as max-heap
        # heapq is a min-heap, so we invert the value to simulate max-heap behavior
        # In a max-heap, the largest element is at the root
        heapq.heappush(self.heap, -val)

    def pop(self):
        return -heapq.heappop(self.heap)

# Time Complexity: O(log n) for both push and pop operations
# Space Complexity: O(n) for storing the heap elements, where n is the number of elements in the heap
# Accessing the largest element is O(1) since it's always at the root of the heap


# Example usage
if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.push(5)
    max_heap.push(1)
    max_heap.push(3)
    max_heap.push(8)
    max_heap.push(2)

    print("Max Heap:", [-x for x in max_heap.heap])  # Internally it maintains the heap property
    print("Largest Element:", max_heap.pop())
    print("Max Heap after removal:", [-x for x in max_heap.heap])
