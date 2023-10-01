class Solution:
    def reverseWords(self, s: str) -> str:
        a=s[::-1].split() 
        a=a[::-1] 
        return " ".join(a)
    
    
        
        
