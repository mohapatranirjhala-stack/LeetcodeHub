# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        # Initialize two pointers
        # By starting fast at head.next.next, slow will stop exactly one node BEFORE the middle.
        slow = head
        fast = head.next.next
        
        # Move fast by 2 steps and slow by 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # slow is now pointing to the node preceding the middle node.
        # Delete the middle node by skipping it.
        slow.next = slow.next.next
        
        return head