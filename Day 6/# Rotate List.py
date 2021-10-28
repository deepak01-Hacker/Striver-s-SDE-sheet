# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        
        if head == None or k == 0:
            return head
        
        temp = head
        length = 0
        last = None

        
        while(temp):
            length += 1
            last = temp
            temp = temp.next
        
        k = k%length
        
        if k == 0:
            return head
        
        temp = head
        k = length-k
        
        while(k > 1):
            k -= 1
            temp = temp.next
        
        print(temp.val)
        newHead = temp.next 
        temp.next = None
        
        last.next = head
        
        return newHead
            
            
    
        
