#Day 2


#Problem : Find the Duplicate Number
# 
# 

class Solution(object):
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            ele = nums[i] if nums[i] > 0 else nums[i]*-1
            
            if nums[ele-1] < 0:
                return ele
            
            nums[ele-1] = nums[ele-1]*-1
        return -1



if __name__ == "__main__":
    nums = [1,3,4,2,2]

    obj1 = Solution()

    print(obj1.findDuplicate(nums))
