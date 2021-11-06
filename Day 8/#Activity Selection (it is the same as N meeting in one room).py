#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        
        q = []
        for i in range(len(start)):
            q.append([start[i],end[i]])
        
        q.sort(key=lambda x:x[1])
        
        last = -1
        meetings = 0
        
        
        for st,en in q:
            if st > last:
                meetings += 1
                last = en
        return meetings

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends
