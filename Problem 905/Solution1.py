class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[e],nums[i]=nums[i],nums[e]
                e+=1
        return nums
        
