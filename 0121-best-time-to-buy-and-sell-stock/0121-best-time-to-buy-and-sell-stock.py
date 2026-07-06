class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p,max_prof=float('inf'),0
        for p in prices:
            min_p=min(min_p,p)
            max_prof=max(max_prof, p-min_p)
        return max_prof