#Day 2


#Problem : Find the Duplicate and Repeated Number
# 
# 

class Solution(object):
    def findDuplicateAndRepeating(self, nums):
        res = [-1,-1] # missing element , repeated

        for i in range(len(nums)):
            ele = nums[i] if nums[i] > 0 else nums[i]*-1
            
            if nums[ele-1] < 0:
                res[-1] = ele
            else:
                nums[ele-1] = nums[ele-1]*-1

        for i in range(len(nums)):
            if nums[i] > 0 :
                res[0] = i+1
                break

        return res[::-1]



if __name__ == "__main__":
    nums = [3, 1, 2, 5, 3] 

    obj1 = Solution()

    print(obj1.findDuplicateAndRepeating(nums))
