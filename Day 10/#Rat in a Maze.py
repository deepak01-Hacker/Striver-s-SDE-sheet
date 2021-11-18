
row = [0,0,1,-1]
col = [1,-1,0,0]

def isSafe(mat,r,c):
    return True if r >= 0 and c >= 0 and r < len(mat) and c < len(mat[0]) and mat[r][c] == 1 else False


def paths(mat,r,c,ans,temp):
    if r == len(mat)-1 and c == len(mat[0])-1 and mat[r][c] == 1:
        ans.append(temp)
        return
    mat[r][c] = -1

    if isSafe(mat,r+1,c):
        paths(mat,r+1,c,ans,temp+"D")

    if isSafe(mat,r-1,c):
        paths(mat,r-1,c,ans,temp+"U")

    if isSafe(mat,r,c+1):
        paths(mat,r,c+1,ans,temp+"R")

    if isSafe(mat,r,c-1):
        paths(mat,r,c-1,ans,temp+"L")

    mat[r][c] = 1

def findPath(mat):
    ans = []

    paths(mat,0,0,ans,"")

    print(ans)




if __name__ == "__main__":
    mat = [[1, 0, 0, 0],
          [1, 1, 0, 1], 
          [1, 1, 0, 0],
          [0, 1, 1, 1]]

    findPath(mat)
