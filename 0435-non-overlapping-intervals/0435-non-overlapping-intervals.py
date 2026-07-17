class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        # Tracks the end time of the last added non-overlapping interval
        last_end = float('-inf')
        
        for start, end in intervals:
            if start >= last_end:
                # No overlap: update the end boundary to this interval's end
                last_end = end
            else:
                # Overlap detected: we must remove this interval
                removals += 1
                
        return removals