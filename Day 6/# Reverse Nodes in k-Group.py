# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverseKGroup(self,head, k):
        if (head is None or k == 1):
            return head

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        nex = dummy
        pre = dummy

        count = 0

        while(curr.next):
            curr = curr.next
            count += 1
        
        headis = False
        while(count >= k):
            curr = pre.next
            nex = curr.next

            for i in range(1,k):
                curr.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = curr.next
            
            st = pre.next
            pre = curr
            count -= k
            
            if headis == False:
                dummy = st
                headis = True
            
            
            
        return dummy
        
