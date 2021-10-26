# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node
        prev = node
        while(temp.next):
            st = temp.val
            temp.val = temp.next.val
            temp.next.val = st
            
            prev = temp
            temp = temp.next
        
        prev.next = None
        
        
