map = {}

class Solution(object):
    
    def isValid(self,s):
        return s == s[::-1]
    
    def util(self,s,temp,ans):
        if s == "":
            ans.append(tuple(temp))
            return True
        
        for i in range(1,len(s)+1):
            
            if s[:i] in map or self.isValid(s[:i]):
                
                map[s[:i]] = True

                temp.append(s[:i])
                
                self.util(s[i:],temp,ans)
                
                temp.pop()
    
    def partition(self, s):
        if s == "":
            return []
        ans = []
        
        self.util(s,[],ans)
        return ans
        
