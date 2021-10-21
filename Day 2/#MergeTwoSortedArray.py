#Day 2


#Problem : Merge two sorted array in O(1) Space 
# 
# 


#  O(m1.n1)
def setOrder(a2):
    ele = a2[0]

    for i in range(len(a2)-1):
        if a2[i+1]>ele:
            a2[i] = ele
            return
        else:
            a2[i] = a2[i+1]
    
    a2[-1] = ele
    
    
    

def merge(a1,a2):
    m1 = len(a1)
    n1 = len(a2)

    if m1 == 0 or n1 == 0:
        return

    i = 0

    while(i<m1):
        if a1[i] > a2[0]:
            a1[i],a2[0] = a2[0],a1[i]
            setOrder(a2)

        i += 1


#Best Case Log2 N.O(N)

def mergeBest(a1,a2):
    m1 = len(a1)
    n1 = len(a2)

    if m1 == 0 or n1 == 0:
        return

    gap = (m1+n1)//2

    while(gap):

        j = -1
        j_Nxt = -1

        i_ = -1
        i_Nxt = -1
        for i in range((m1+n1-gap)):
            if i+gap >= m1 :
                i_Nxt = -1
                j_Nxt = i+gap-m1 
            else :
                i_Nxt = i+gap
                j_Nxt = -1

            if i < m1 :
                i_ = i
                j = -1
            
            else :
                j = i-m1
                i_ = -1

            print(i_,j,i_Nxt,j_Nxt)

            if i_ >-1 and i_Nxt > -1:
                if a1[i_] > a1[i_Nxt]:
                    a1[i_],a1[i_Nxt] = a1[i_Nxt],a1[i_]

            elif i_ > -1 and j_Nxt > -1:
                if a1[i_] > a2[j_Nxt]:
                    a1[i_],a2[j_Nxt] = a2[j_Nxt],a1[i_]
                    print("True")

            elif j > -1 and j_Nxt > -1:
                if a2[j] > a2[j_Nxt]:
                    a2[j],a2[j_Nxt] = a2[j_Nxt],a2[j]


        gap = gap//2





if __name__ == "__main__":
    a1 = [1,4,7,8,10]
    a2 = [2,3,9]


    mergeBest(a1,a2)

    print(a1,end=" ")
    print(a2,end=" ")
