class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=set()
        for i,n in enumerate(nums):
            l,r=i+1,len(nums)-1
            while l<r:
                s=n+nums[l]+nums[r]
                if s==0: res.add((n,nums[l],nums[r]))
                if s<=0: l+=1
                if s>=0: r-=1
        return list(res)