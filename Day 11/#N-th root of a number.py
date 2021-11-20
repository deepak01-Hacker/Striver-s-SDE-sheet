#0000000000000000000000000000000000000000 Binary Search 0000000000000000000000000000000000000000000000000000000000000000

#The N-th root of an integer

def nthRoot(a,n):
    left = 1
    right = a

    while(right-left > 0.001):
        numMid = (left+right)/2

        if numMid**n == a:
            return numMid

        if numMid **n > a:
            right = numMid
        else:
            left = numMid
    return numMid


if __name__ == "__main__":
    A = 81
    N = 4

    print(nthRoot(A,N))
   
 # 000000000000000000000000000000000000000000000000000000000 Newton Method 00000000000000000000000000000000000000000000000
import math
import random
 
# method returns Nth power of A
def nthRoot(A,N):
 
    # initially guessing a random number between
    # 0 and 9
    xPre = random.randint(1,101) % 10
  
    #  smaller eps, denotes more accuracy
    eps = 0.001
  
    # initializing difference between two
    # roots by INT_MAX
    delX = 2147483647
  
    #  xK denotes current value of x
    xK=0.0
  
    #  loop until we reach desired accuracy
    while (delX > eps):
 
        # calculating current value from previous
        # value by newton's method
        xK = ((N - 1.0) * xPre +
              A/pow(xPre, N-1)) /N
        delX = abs(xK - xPre)
        xPre = xK;
         
    return xK
 
# Driver code
N = 4
A = 81
nthRootValue = nthRoot(A, N)
 
print("Nth root is ", nthRootValue)

    
