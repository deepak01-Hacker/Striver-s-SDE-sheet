#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        queue = []
        #queue.append([-1,-1])
    
        for i in range(len(start)):
            queue.append([start[i],end[i]])
        
        queue.sort(key=lambda x:x[1])
    
        countMeeting = 0
        lastTime = -1
    
        for i in range(len(queue)):
            if lastTime < queue[i][0]:
                countMeeting += 1
                lastTime = queue[i][1]
        return countMeeting

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
