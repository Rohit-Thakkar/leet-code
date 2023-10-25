def invert(num):
    if num == 1 :return 0
    if num == 0 :return 1 
class Solution:

    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 or k == 1 :
            return 0 
        if n == 2 and k == 1 :
            return 0 
        if n == 2 and k == 2 :
            return 1 
        if k <= 2 **(n-2):
            return self.kthGrammar(n-1,k)
        elif k > 2**(n-2):
            return invert(self.kthGrammar(n-1,k -(2**(n-2))))
