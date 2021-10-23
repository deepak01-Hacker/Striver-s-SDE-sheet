class Solution(object):
    def majorityElement(self, nums):

        # majority element_count > len(nums) //3
        
        ct1 = 0
        ct2 = 0
        
        ele1 = 0
        ele2 = 0
        
        for ele in nums:
            
            if ele1 == ele:
                ct1 += 1
                
            elif ele2 == ele:
                ct2 += 1
                
            elif ct1 == 0:
                ele1 = ele
                ct1 = 1
                
            elif ct2 == 0:
                ele2 = ele
                ct2 = 1
                
            else:
                ct1 -= 1
                ct2 -= 1
                
        ans = []
        if nums.count(ele1) > len(nums)//3:
            ans.append(ele1)
            
        if ele1 != ele2 and nums.count(ele2) > len(nums)//3:
            ans.append(ele2)
            
        return ans
                
