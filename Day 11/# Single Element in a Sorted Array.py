class Solution(object):
    def singleNonDuplicate(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(arr)-1

        while(left<=right):
            mid = (left+right)//2

            if ((mid-1 >= 0 and arr[mid-1] != arr[mid]) or (mid-1 < 0 )) and ((mid+1 < len(arr) and arr[mid+1] != arr[mid]) or (mid+1 >= len(arr) )):
                return arr[mid]

            index = mid+1 if mid+1 < len(arr) and arr[mid] == arr[mid+1] else mid


            if ((index-left)+1)%2 != 0:
                right = index-1
            else:
                left = index+1

        return arr[left]

