# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[(n.val,i,n) for i,n in enumerate(lists) if n]
        heapq.heapify(heap)
        cur=dummy=ListNode()
        while heap:
            val,i,node=heapq.heappop(heap)
            cur.next=node
            cur =cur.next
            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        return dummy.next
        
        