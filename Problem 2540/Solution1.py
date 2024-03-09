class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        arr1 = 0
        arr2 = 0

        m, n = len(nums1), len(nums2)

        while arr1 < m and arr2 < n:
            if nums1[arr1] == nums2[arr2]:
                return nums1[arr1]
            elif nums1[arr1] < nums2[arr2]:
                arr1 += 1
            else:
                arr2 += 1
        
        return -1
    
