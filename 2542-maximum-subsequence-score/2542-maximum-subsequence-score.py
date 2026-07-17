class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        
        min_heap = []
        current_sum = 0
        max_score = 0
        
        # Step 2: Iterate through the sorted pairs
        for n1, n2 in pairs:
            # Add the current nums1 element to the heap and the running sum
            heapq.heappush(min_heap, n1)
            current_sum += n1
            
            # If our heap size exceeds k, pop the smallest element to optimize the sum
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
                
            # If we have exactly k elements, update the max score
            # Since pairs are sorted descending by nums2, n2 is guaranteed to be the minimum
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * n2)
                
        return max_score