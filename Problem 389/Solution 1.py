class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(ord(l) for l in t) - sum(ord(l) for l in s))
        
