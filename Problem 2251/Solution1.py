class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        def lbsearch(arr, x, l=0, r=None):
            if r is None:
                r = len(arr)
            l -= 1
            r -= 1
            while l + 1 != r:
                m = (l + r) // 2
                if arr[m] < x:
                    l = m
                else:
                    r = m
            return r
        
        def rbsearch(arr, x, l=0, r=None):
            if r is None:
                r = len(arr)
            while l + 1 != r:
                m = (l + r) // 2
                if arr[m] > x:
                    r = m
                else:
                    l = m
            return l
        
        def get_bounds(i):
            bounds = [0] * 2
            for bound in [0, 1]:
                if i > flowers[bound][-1]:
                    bounds[bound] = length
                elif i < flowers[bound][0]:
                    bounds[bound] = 0
                else:
                    bounds[bound] = (rbsearch, lbsearch)[bound](flowers[bound], i) + (bound == 0)
            return bounds
            
        length = len(flowers)
        flowers[:] = list(zip(*flowers))
        flowers[:] = [sorted(flowers[bound]) for bound in [0,1]]

        ans = [None] * len(people)
        for i, num in enumerate(people):
            a, b = get_bounds(num)
            ans[i] = a-b
        return ans
