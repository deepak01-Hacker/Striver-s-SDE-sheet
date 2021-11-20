
# Matrix-Median - using Binary Search

def countSmaller(A,ele):
    low = 0
    high = len(A)-1

    while(low<=high):
        mid = (low+high) >> 1

        if A[mid] <= ele:
            low = mid+1
        else:
            high = mid-1
    
    return low



def findMedian(mat):

    #   1,3,5
    #   2,6,9
    #   3,6,9


    low = 0
    high = 10**9

    while(low<=high):

        mid = (low+high) >> 1
        cntMin = 0

        for i in range(len(mat)):
            cntMin += countSmaller(mat[i],mid)
        
        if cntMin <= (len(mat)*len(mat[0]))//2 :
            low = mid+1
        else:
            high = mid-1

    return low






if __name__ == "__main__":
    mat =  [[1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]]
    
    print(findMedian(mat))
