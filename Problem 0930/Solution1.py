class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0

        leadingZeros, start, total = 0, 0, 0
        for end in range(len(nums)):
            total += nums[end]

            while start < end and (nums[start] == 0 or total > goal):
                total -= nums[start]
                leadingZeros = (leadingZeros + 1) if nums[start] == 0 else 0
                start += 1

            if total == goal:
                result += (leadingZeros + 1)

        return result



            
