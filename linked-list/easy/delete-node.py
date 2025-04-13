# There is a singly-linked list head and we want to delete a node node in it.
def deleteNode(node):
    # Since the node to be deleted is not a tail node, we can copy the value of the next node to the current node and then delete the next node.
    # Copy the value of the next node to the current node

    # If the node to be deleted is the last node, we cannot delete it directly.
    # We can only delete the node if it is not the last node.
    if node.next is None:
        node.val = None
        return
    
    # Copy the value of the next node to the current node
    node.val = node.next.val
    # Delete the next node
    node.next = node.next.next
    # The node is deleted, and the current node now contains the value of the next node.

# Example usage:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Creating a linked list: 4 -> 5 -> 1 -> 9
node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4
# Deleting node with value 5
deleteNode(node3)
# Printing the modified linked list
current = node1
while current:
    print(current.val, end=" -> ")
    current = current.next
# Output: 4 -> 1 -> 9 ->

# The time complexity is O(1) because we are only performing a constant number of operations.
# The space complexity is O(1) because we are not using any additional data structures.