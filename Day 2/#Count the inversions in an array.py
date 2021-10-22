#Day 2

#Problem : Count the inversions in an array
# 

#o(n2)

def inversionCount(arr):
    inversion = 0

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                inversion += 1
    return inversion

#BEst O(nlogn)

def merge(arr,temp,left,mid,right):
    i = left
    j = mid
    k = left

    inv_count = 0

    while(i <= mid-1 and j <= right):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1

            inv_count += (mid-i)

        k += 1

    while(i<=mid-1):
        temp[k] = arr[i]
        k += 1
        i += 1

    while(j <= right):
        temp[k] = arr[j]
        k += 1
        j += 1
    
    for i in range(left,right+1):
        arr[i] = temp[i]
    
    return inv_count

def inversionCountBest(arr,left,right,temp):
    inv_count = 0

    if (left<right):

        mid = (left+right)//2

        inv_count += inversionCountBest(arr,left,mid,temp)
        inv_count += inversionCountBest(arr,mid+1,right,temp)

        inv_count += merge(arr,temp,left,mid+1,right)
    
    return inv_count



if __name__ == "__main__":
    arr = [3,1,2,5]

    temp = [0]*len(arr)
    print(inversionCountBest(arr,0,len(arr)-1,temp))
