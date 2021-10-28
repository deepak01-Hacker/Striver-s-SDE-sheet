#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(head):
    dummy = Node(0)
    dummy.next = head

    while(head.next):

        first = head.bottom
        last = head.next

        newb = None
        temp = newb

        while(first and last):
            if (first.data <= last.data):
                nexts = first.bottom

                if newb == None:
                    newb = first
                    temp = newb
                else:
                    temp.bottom = first
                    temp = temp.bottom

                first = nexts

            else:
                nexts = last.bottom
                
                if newb == None:
                    newb = first
                    temp = newb
                else:
                    temp.bottom = last
                    temp = temp.bottom

                last = nexts

            temp.bottom = None
        
        while(first):
            nexts = first.bottom

            temp.bottom = first
            temp = temp.bottom
            temp.bottom = None

            first = nexts
        
        while(last):
            nexts = last.bottom
            
            temp.bottom = last
            temp = temp.bottom
            temp.bottom = None

            last = nexts
        
        head.bottom = newb
        nexts = head.next.next
        head.next = None
        head.next = nexts

    return dummy.next


#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
        

def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
        
    print()


if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]
        
        arr=[int(x) for x in input().strip().split()]
        temp=None
        tempB=None
        pre=None
        preB=None
        
        flag=1
        flag1=1
        listo=[int(x) for x in input().strip().split()]
        it=0
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag is 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1
                
            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 is 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        root=flatten(head)
        printList(root)
        
        t-=1
            
# } Driver Code Ends
