# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
def hascycle(head):
    # Initialize two pointers, slow and fast
    slow = fast = head

    # Traverse the list with two pointers
    while fast and fast.next:
        slow = slow.next  # Move slow pointer one step
        fast = fast.next.next  # Move fast pointer two steps

        # If slow and fast pointers meet, there is a cycle
        if slow == fast:
            return True

    return False  # No cycle found
# Example usage:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Creating a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4) 
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4  
node4.next = node5
node5.next = node3  # Creating a cycle (5 -> 3)
# Printing the original linked list
# current = node1
# while current:
#     print(current.val, end=" -> ")
#     current = current.next
# print()
# Checking if the linked list has a cycle
result = hascycle(node1)
if result:
    print("The linked list has a cycle.")
else:
    print("The linked list does not have a cycle.")


# The time complexity is O(n), where n is the number of nodes in the linked list.
# The space complexity is O(1) because we are using a constant amount of extra space.