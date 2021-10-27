# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        
        #first find middle and reverse the linkedList from middle
        slow = head
        fast = head.next
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        
        while(curr):
            nexts = curr.next
            curr.next = prev
            prev = curr
            
            curr = nexts
        
        slow.next = prev
        
        while(head and prev and head != prev ):
            if (head.val != prev.val):
                return False
            
            head = head.next
            prev = prev.next
        return True
        
