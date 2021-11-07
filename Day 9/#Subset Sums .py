#User function Template for python3
class Solution:
    
    def util(self,arr,result,start,sum):
    
        result.append(sum)
    
        if start >= len(arr):
            return
    
        for i in range(start,len(arr)):
            self.util(arr,result,i+1,sum+arr[i])
    
	def subsetSums(self, arr, N):
	    result = []
	    self.util(arr,result,0,0)
	    
	    return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends
