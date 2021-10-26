# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, headofLL, n):
        if headofLL == None:
            return None

        head = headofLL
        lengthOfLinkedList = 0
        tempHead = head

        while(tempHead):
            lengthOfLinkedList += 1
            tempHead = tempHead.next

        if n == lengthOfLinkedList:
            headofLL = headofLL.next
            return head.next

        prev  = None
        while(head):
            if lengthOfLinkedList == n:
                prev.next = head.next
                return headofLL
            prev = head
            head = head.next
            lengthOfLinkedList -= 1

        return headofLL
        
        
