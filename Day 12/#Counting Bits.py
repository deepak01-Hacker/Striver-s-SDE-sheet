class Solution(object):
    def countBits(self, n):
        res =[0]*(n+1)
        
        for i in range(1,n+1):
            if i%2 != 0:
                res[i] = res[i//2]+1
            else:
                res[i] = res[i//2]
        return res
