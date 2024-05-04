def is_safe(mat,r,c):
    for i in range(r):
        if mat[i][c]=='Q':
            return False
        if c-r+i >=0 and  mat[i][c-r+i]=='Q':
            return False
        if c+r-i<len(mat) and mat[i][c+r-i]=='Q':
            return False
    return True
def n_queen(mat,r):
    if r==len(mat):
        printsol(mat)
        return
    for i in range(len(mat)):
        if is_safe(mat,r,i):
            mat[r][i]='Q'
            n_queen(mat,r+1)
            mat[r][i]='-'
def printsol(mat):
    for r in mat:
        print(''.join(r))
    print()
if __name__=='__main__':
    print("Enter the number of queen: ")
    n=int(input())
    mat=[['-' for _ in range(n)]for _ in range(n)]
    n_queen(mat,0)