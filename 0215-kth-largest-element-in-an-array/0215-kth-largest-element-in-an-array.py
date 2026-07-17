import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize an empty min-heap
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            
            # If the heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # The root of the heap is the kth largest element
        return min_heap[0]