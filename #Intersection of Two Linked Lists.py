# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def preProcess(self,temp1):
        
        while(temp1):
            temp1.val = temp1.val*-1
            temp1 = temp1.next
            
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        self.preProcess(headA)
        
        res = None
        while(headB):
            if headB.val < 0 :
                res = headB
                break
            headB = headB.next
                
        self.preProcess(headA)
        return res
