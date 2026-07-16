# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Initialize pointers
        odd = head          # Tracks the current node in the odd list
        even = head.next    # Tracks the current node in the even list
        evenHead = even     # Saves the start of the even list to connect later
        
        # Traverse the list until we reach the end of either list
        while even and even.next:
            odd.next = even.next   # Connect current odd node to next odd node
            odd = odd.next         # Move odd pointer forward
            
            even.next = odd.next   # Connect current even node to next even node
            even = even.next       # Move even pointer forward
            
        # Connect the end of the odd list to the head of the even list
        odd.next = evenHead
        
        return head