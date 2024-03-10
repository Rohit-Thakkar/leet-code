class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hashmap ={}
        intersection = []

        for i in nums1:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i]=1
        
        for i in nums2:
            if i in hashmap:
                intersection.append(i)
                del hashmap[i]
        
        return intersection


        
