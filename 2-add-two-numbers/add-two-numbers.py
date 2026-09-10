# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head acts as a placeholder to easily return the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop continues while there are nodes to process or a carry remains
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            out_val = total_sum % 10
            
            # Create a new node with the calculated digit
            current.next = ListNode(out_val)
            current = current.next
            
            # Move to the next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next
        