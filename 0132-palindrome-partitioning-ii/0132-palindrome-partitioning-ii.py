class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[-1]*n
        dp[-1]=1
        dp=dp+[0]
        for k in range(n-2,-1,-1):
            minn=float('inf')
            for j in range(k+1,n+1):
                if s[k:j]==s[k:j][::-1]:
                    minn=min(minn,1+dp[j])
            dp[k]=minn
        return dp[0]-1
        #return minn
        