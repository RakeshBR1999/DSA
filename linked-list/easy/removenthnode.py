# Given the head of a linked list, remove the nth node 
# from the end of the list(Removing the 2nd node from the end (node with value 4)) and return its head.
def removenthnode(head, n):
    # Create a dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move both pointers until the first pointer reaches the end
    while first:
        first = first.next
        second = second.next

    # Remove the nth node from the end
    second.next = second.next.next

    return dummy.next

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
# Removing the 2nd node from the end (node with value 4)
new_head = removenthnode(node1, 2)
# Printing the modified linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
# Output: 1 -> 2 -> 3 -> 5 ->

# The time complexity is O(L), where L is the length of the linked list.
# The space complexity is O(1) because we are using a constant amount of extra space.