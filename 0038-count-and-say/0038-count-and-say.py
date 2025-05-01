class Solution:
    def countAndSay(self, n: int) -> str:
        l=['1']
        while len(l)!=n:
            count=0
            s=''
            r=''
            prev=l[-1]
            for i in range(len(prev)):
                if count==0:
                    s+=prev[i]
                    count=1
                elif prev[i]==s[-1]:
                    count+=1
                elif prev[i]!=s[-1]:
                    r+=str(count)+str(prev[i-1])
                    s+=prev[i]
                    count=1
                if i==len(prev)-1:
                    r+=str(count)+str(prev[i])
            l.append(r)
        return l[n-1]
