class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        resMax = 0
        
        for ele in nums:
            cnt = cnt+1 if ele == 1 else 0
            
            resMax = max(cnt,resMax)
        return resMax
        
