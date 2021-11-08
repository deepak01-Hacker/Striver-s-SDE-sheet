class Solution(object):
   
    def getPermutation(self, n, k):
        fact = [1,1,2,6,24,120,720,5040,40320,362880]
        ans = ""
        digits = [i for i in range(1,n+1)]

        while(n):
            index_ = k//(fact[n-1])
            if k%(fact[n-1]) == 0:
                index_ -= 1
            ans += str(digits[index_])
            removeIn = digits.index(digits[index_])
            digits.pop(removeIn)

            k = k - (index_*fact[n-1])
            n -= 1
        return ans


        
        
