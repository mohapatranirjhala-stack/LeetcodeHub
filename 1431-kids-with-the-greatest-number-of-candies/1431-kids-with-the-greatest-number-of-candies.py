class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        limit = max(candies) - extraCandies
        return [c>= limit for c in candies]
        