class Solution(object):
    def fourSum(self, nums, tr):
        res = set()
        
        nums.sort()
        
        n = len(nums)
        
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j+1
                right = n-1 
                
                while(left<right):
                    
                    currentSum = nums[i]+nums[j]+nums[left]+nums[right]
                    
                    if currentSum == tr:
                    
                        res.add((nums[i],nums[j],nums[left],nums[right]))
                        left += 1
                        
                    elif currentSum < tr:
                        left += 1
                    else:
                        right -= 1
        return list(res)
                        
