class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        cur_min=cur_max=1
        for n in nums:
            cur_max,cur_min=max(n,n*cur_max,n*cur_min),min(n,n*cur_max,n*cur_min)
            res=max(res,cur_max)
        return res
        