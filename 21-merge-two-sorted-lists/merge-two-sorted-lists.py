# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 1. Initialize a dummy node and a current pointer
        dummy = ListNode(-1)
        current = dummy
        
        # 2. Traverse both lists until one runs out
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # 3. Append the remaining nodes of the non-empty list
        current.next = list1 if list1 else list2
        
        # 4. Return the head of the newly merged list
        return dummy.next
