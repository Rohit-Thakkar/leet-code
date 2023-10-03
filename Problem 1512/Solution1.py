class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # count the number of times a number appers
        good = 0
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for key in count:
            n = count[key]
            good += n*(n-1)//2
        return good
