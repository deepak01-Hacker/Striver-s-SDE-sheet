class Solution(object):
    
    def merge(self,nums,left,mid,right):
        i = left
        j = mid
        reverse_count = 0
        for i in range(left,mid):
            while(j<=right and nums[i] > 2*nums[j]):
                j += 1
            reverse_count += (j-mid)


        temp = []
        i = left
        j = mid

        while(i<=mid-1 and j <= right):
            if nums[i]<=nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])

                j += 1


        while(i<=mid-1):
            temp.append(nums[i])
            i += 1

        while(j<=right):
            temp.append(nums[j])
            j += 1

        for t in range(left,right+1):
            nums[t] = temp[t-left]

        return reverse_count


    def util(self,nums,left,right):
        reverse_count = 0

        if (left<right):
            mid = (left+right)//2

            reverse_count += self.util(nums,left,mid)
            reverse_count += self.util(nums,mid+1,right)

            reverse_count += self.merge(nums,left,mid+1,right)

        return reverse_count

    def reversePairs(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.util(nums,0,len(nums)-1)
        
