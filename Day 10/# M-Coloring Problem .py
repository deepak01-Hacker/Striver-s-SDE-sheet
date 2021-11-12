
def isSafe(graph,color,node,N,col):

    for k in range(N):
        if k != node and graph[k][node] == 1 and col == color[k]:
            return False
    return True



def util(graph,color,N,node,M):

    if (node == N):
        return True
    
    for i in range(1,M+1):

        if isSafe(graph,color,node,N,i):
            
            color[node] = i

            if(util(graph,color,N,node+1,M)):
                return True
            
            color[node] = 0

    return False





def graphColoring(graph, M, N):
    
    color = [0]*N

    return util(graph,color,N,0,M)
    
    #your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends
