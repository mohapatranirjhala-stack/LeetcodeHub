class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Base variables representing the minimum cost to reach the last two steps
        prev2 = 0  # Cost to reach two steps back
        prev1 = 0  # Cost to reach one step back
        
        # Calculate minimum cost for each step up to the top floor
        for i in range(2, len(cost) + 1):
            current = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2 = prev1
            prev1 = current
            
        return prev1