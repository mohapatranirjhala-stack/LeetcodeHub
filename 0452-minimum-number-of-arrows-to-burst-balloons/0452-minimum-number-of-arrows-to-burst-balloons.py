class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        # Sort the balloons based on their end coordinates
        points.sort(key=lambda x: x[1])
        
        # Start with 1 arrow placed at the end of the first balloon
        arrows = 1
        curr_arrow_pos = points[0][1]
        
        for i in range(1, len(points)):
            start, end = points[i]
            
            # If the current balloon starts after the last arrow position,
            # we must shoot a new arrow.
            if start > curr_arrow_pos:
                arrows += 1
                curr_arrow_pos = end
                
        return arrows