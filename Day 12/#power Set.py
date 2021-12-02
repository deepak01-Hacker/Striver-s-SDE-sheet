#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
	    result = []
		
		for num in range(0,2**len(s)):
		    
		    strs = ''
		    
		    for it in range(0,num):
		        
		        if (num &(1<<it)):
		            
		            strs += s[it]
    	    result.append(strs)
		
		return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends
