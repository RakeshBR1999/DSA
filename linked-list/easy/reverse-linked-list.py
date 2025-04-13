# Given the head of a singly linked list, reverse the list, and return the reversed list.
def reverseList(head):
    # Initialize three pointers: prev, curr, and next
    prev = None
    curr = head

    # Traverse the list and reverse the links
    while curr:
        temp = curr.next  # Store the next node
        curr.next = prev  # Reverse the link
        prev = curr  # Move prev to current node
        curr = temp  # Move to the next node

    return prev  # Return the new head of the reversed list
# Example usage:        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# Printing the original linked list
current = node1
while current:
    print(current.val, end=" -> ")
    current = current.next
# printnewline()
print()
# Reversing the linked list
new_head = reverseList(node1)
# Printing the reversed linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
# Output: 5 -> 4 -> 3 -> 2 -> 1 ->

# The time complexity is O(L), where L is the length of the linked list.
# The space complexity is O(1) because we are using a constant amount of extra space.

