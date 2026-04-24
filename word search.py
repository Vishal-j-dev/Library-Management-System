def dfs(board,i,j,row,col,word,index):
    if index==len(word)-1:
        return True
    if i<0 or j<0 or i>=row or j>=col or board[i][j]!=word[index]:
        return False
    temp=board[i][j]
    board[i][j]="#"
    found=False
    dir=[[0,1],[0,-1],[-1,0],[1,0]]
    for di,dj in dir:
        ni,nj=i+di,j+dj
        if dfs(board,ni,nj,row,col,word,index+1):
            return True
    board[i][j]=word[index]
    return False
        

board=[['g','k','m','f','i'],['t','g','s','e','n',],['o','c','t','c','k'],['o','m','k','o','l'],['t','r','e','d','k']]
word = "finestcoder"  
row=len(board)
col=len(board[0])
index=0
flag = False
for i in range(row):
    for j in range(col):
        if board[i][j]==word[0]:
            if(dfs(board,i,j,row,col,word,index)):
                flag=True
                break
         
        if flag:
            break
        print(board[i][j],end=" ")
    print()
print(board)