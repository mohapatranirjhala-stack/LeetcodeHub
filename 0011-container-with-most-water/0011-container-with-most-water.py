class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r, max_a = 0, len(height) - 1, 0
        while l < r:
            max_a = max(max_a, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]: l += 1
            else: r -= 1
        return max_a