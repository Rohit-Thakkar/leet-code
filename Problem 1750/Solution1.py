class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) >= 2:
            if s[0] == s[len(s)-1]:
                s = s.strip(s[0])
            else: 
                break
        return len(s) 
