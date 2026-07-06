class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res,p,s=[1]*len(nums),1,1
        for i,n in enumerate(nums):
            res[i],p=p,p*n
        for i in range(len(nums)-1,-1,-1):
            res[i],s=res[i]*s,s*nums[i]
        return res
        