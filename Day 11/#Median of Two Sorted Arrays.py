class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums2)<len(nums1)):
            return self.findMedianSortedArrays(nums2,nums1)


        low = 0
        high = len(nums1)

        while(low<=high):

            cut1 = (low+high) >> 1
            cut2 = int((len(nums1)+len(nums2)+1)/2) - cut1

            left1 = nums1[cut1-1] if cut1 != 0 else -10**9
            right1 = nums1[cut1] if cut1 != len(nums1) else 10**9

            left2 = nums2[cut2-1] if cut2 != 0 else -10**9
            right2 = nums2[cut2] if cut2 != len(nums2) else 10**9

            if (left1<=right2 and left2 <= right1):

                if (len(nums1)+len(nums2))%2 == 0:
                    t = (max(left1,left2)+min(right1,right2))
                    #print(left1,left2,right1,right2)
                    return float(t)/2
                return max(left1,left2)

            elif (left1 > right2):
                high = cut1-1
            else:
                low = cut1+1

                
        return 0.0
