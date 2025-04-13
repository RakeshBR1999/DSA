# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
def isPalindrom(head):
    if not head or not head.next:
        return True

    # Step 1: Find middle using slow and fast pointer
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Step 3: Compare two halves
    left, right = head, prev
    while right:  # Only need to compare right half
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
# Example usage:    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creating a linked list: 1 -> 2 -> 3 -> 2 -> 1
node1 = ListNode(1)
node2 = ListNode(2)         
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)     
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# Printing the original linked list
current = node1
while current:
    print(current.val, end=" -> ")
    current = current.next
print()
# Checking if the linked list is a palindrome
result = isPalindrom(node1)
if result:
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")

# Time complexity: O(n), where n is the number of nodes in the linked list. 
# Space complexity: O(1), as we are using a constant amount of extra space.