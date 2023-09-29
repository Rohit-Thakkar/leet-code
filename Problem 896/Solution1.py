class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True 
        num = nums[0]
        def minf(nums):
            nonlocal num
            for i in range(1,len(nums)):
                if nums[i]<num:
                    return False
                num = nums[i]
            return True
        def maxf(nums):
            nonlocal num
            for i in range(1,len(nums)):
                if nums[i]>num:
                    return False
                num = nums[i]
            return True
        if nums[0]>nums[-1]:
            return maxf(nums)
        else:
            return minf(nums)
