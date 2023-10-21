class Solution:
    def constrainedSubsetSum(self, nums, k):
        maxTillThis = nums.copy()
        maxSbSqUptSzK = deque()
        res = maxTillThis[0]
        for indx in range(len(maxTillThis)):
            maxTillThis[indx] += maxTillThis[maxSbSqUptSzK[0]] if len(maxSbSqUptSzK) > 0 else 0
            res = max(res, maxTillThis[indx])
            while len(maxSbSqUptSzK) > 0 and maxTillThis[indx] > maxTillThis[maxSbSqUptSzK[-1]]:
                maxSbSqUptSzK.pop()
            if maxTillThis[indx] > 0:
                maxSbSqUptSzK.append(indx)
            if indx >= k and len(maxSbSqUptSzK) > 0 and maxSbSqUptSzK[0] == indx - k:
                maxSbSqUptSzK.popleft()
        return res
