"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        newHead = None
        temphead = head

        while(temphead):
            nexts = temphead.next
            newNode = Node(temphead.val)
            temphead.next = newNode
            newNode.next = nexts
            
            temphead = temphead.next.next

        thead = head
        while(thead):
            randomPointer = thead.random
            thead.next.random = randomPointer.next if randomPointer else None

            if newHead == None:
                newHead = thead.next

            thead = thead.next.next
        
        prev = None
        while(head):
            nextss = head.next.next
            nexts = head.next
            if prev:
                prev.next = nexts
            prev = nexts

            head.next = nextss
            head = head.next

        return newHead
