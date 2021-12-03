import math

def findMSB(n):
    tn = math.log2(n)
    i = math.floor(tn)
    return n&(1<<i)
