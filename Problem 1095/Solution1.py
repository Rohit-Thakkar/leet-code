# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
            # Save the length of the mountain array
        length = mountain_arr.length()

            # Find the index of the peak element
        low = 1
        high = length - 2
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < mountain_arr.get(test_index + 1):
                low = test_index + 1
            else:
                high = test_index
        peak = low
        l = 0
        h = peak-1
        minOccur = -1
            # find in left portion
        while l <= h :
            mid = (l+h)//2
            if MountainArray.get(mountain_arr,mid) == target : 
                minOccur = mid
                return minOccur
            elif MountainArray.get(mountain_arr,mid) < target: l = mid+1
            else : h = mid-1
        l = peak
        h = length-1
            # find in right portion
        while l <= h:
            mid = (l+h)//2
            if MountainArray.get(mountain_arr,mid) == target :
                minOccur = mid
                return minOccur
            elif MountainArray.get(mountain_arr,mid) > target : l = mid+1
            else : h = mid-1

        return minOccur
