class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        prev=[0]*m
        for i in range(n):
            temp=[0]*m
            for j in range(m):
                if i==0 and j==0:
                    temp[j]=grid[i][j]
                    continue
                up=left=float("inf")
                if i>0:
                    up=grid[i][j]+prev[j]
                if j>0:
                    left=grid[i][j]+temp[j-1]
                temp[j]=min(up,left)
            prev=temp
        return prev[m-1]
