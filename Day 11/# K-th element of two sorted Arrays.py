#User function Template for python3

class Solution:
    def kthElement(self,  nums1, nums2, n, m, k):
        
        if n<m:
            return self.kthElement(nums2,nums1,m,n,k)
        elif n == 0:
            return nums2[k-1]
        elif m == 0:
            return nums1[k-1]
        
        
        low = max(0,k-m)
        high = min(n,k)
        
        while(low<=high):
        
            cut1 = (low+high) >> 1
            cut2 = k - cut1
        
            left1 = nums1[cut1-1] if cut1 != 0 else -10**32
            right1 = nums1[cut1] if cut1 != len(nums1) else 10**32
            
            #print(cut2-1)
            left2 = nums2[cut2-1] if cut2 > 0 and m > 0 else -10**32
            right2 = nums2[cut2] if cut2 != len(nums2) else 10**32
        
            if (left1<=right2 and left2 <= right1): 
                return max(left1,left2)
        
            elif (left1 > right2):
                high = cut1-1
            else:
                low = cut1+1
        
                
        return 0
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
