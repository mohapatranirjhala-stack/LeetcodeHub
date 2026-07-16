# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Phase 2: Reverse the second half of the list starting from 'slow'
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Phase 3: 'prev' now points to the head of the reversed second half.
        # Compare twins and calculate max twin sum.
        max_sum = 0
        first_half = head
        second_half = prev
        
        while second_half:
            current_twin_sum = first_half.val + second_half.val
            max_sum = max(max_sum, current_twin_sum)
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum