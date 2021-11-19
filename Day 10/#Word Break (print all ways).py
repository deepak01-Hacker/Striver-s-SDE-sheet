
def util(st,n,line,ans,dict):

    for i in range(1,n+1):

        if st[:i] in dict:

            if i == n:

                line += st[:i]
                ans.append(line)
                return 
            
            util(st[i:],n-i,line+st[:i]+" ",ans,dict)



def alldict(st,dict):
    dict = set(dict)

    ans = []

    util(st,len(st),"",ans,dict)

    return ans



if __name__ == "__main__":
    st = "ilikesamsungmobile"
    dict = [ "i", "like", "sam", "sung", "samsung", "mobile", "ice", "and", "cream", "icecream", "man", "go", "mango"]

    print(alldict(st,dict))
