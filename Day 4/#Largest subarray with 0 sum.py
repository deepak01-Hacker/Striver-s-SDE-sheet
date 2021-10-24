#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, nums):
        sum = 0
        map = {}

        longestSubarry = 0

        for i in range(len(nums)):
            sum += nums[i]
            
            if sum in map:
                longestSubarry = max(longestSubarry,i-map[sum])
            else:
                map[sum] = i
            
            if sum == 0:
                longestSubarry = max(longestSubarry,i+1)
        
        
        
        return longestSubarry

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
