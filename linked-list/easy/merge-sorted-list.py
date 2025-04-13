# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

def mergeTwoLists(list1,list2):
    # Create a dummy node to simplify the merging process
    dummy = ListNode(0)
    current = dummy

    # Traverse both lists and merge them in sorted order
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # If one of the lists is not empty, append it to the merged list
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next  # Return the head of the merged linked list
# Example usage:        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Creating two sorted linked lists: 1 -> 2 -> 4 and 1 -> 3 -> 4
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6
# Merging the two linked lists
new_head = mergeTwoLists(node1, node4)
# Printing the merged linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 ->

# The time complexity is O(n + m), where n and m are the lengths of the two linked lists.
# The space complexity is O(1) because we are using a constant amount of extra space.