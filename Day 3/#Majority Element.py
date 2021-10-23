class Solution(object):
    def majorityElement(self, nums):
            # majority element_count > len(nums) //2

        count = 0
        ele = 0

        for i in range(len(nums)):
            if count == 0:
                ele = nums[i]

            if ele == nums[i]:
                count += 1
            else:
                count -= 1
        return ele

