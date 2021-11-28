
from logging import FATAL


def isPossible(stalls,distance,cows):
    prevPoint = stalls[0]
    ct = 1
    prev = stalls[0]

    #print(distance)


    i = 1
    while(i<len(stalls)):
        if stalls[i]-prevPoint >= distance:
            if (prev-prevPoint)-1 > 0 and (prev-prevPoint)-1 <= distance:
                ct += 1
                prevPoint = prev
            elif (prevPoint-prev) <= 0:
                #print(stalls[i],prev,prevPoint,distance)
                return False
        
        prev = stalls[i]

        i += 1
    
    
    return  ct <= distance






def minimumLargestDistance(stalls,cows):

    stalls.sort()

    low = 1
    high = stalls[-1]-stalls[0]

    while(low<=high):

        mid = (low+high) >> 1

        if isPossible(stalls,mid,cows):
            high = mid-1
        else:
            low = mid+1
    
    return mid


if __name__ == "__main__":
    n = 5
    c = 3

    stalls = [1,2,8,4,9] # at index

    print(minimumLargestDistance(stalls,c))
