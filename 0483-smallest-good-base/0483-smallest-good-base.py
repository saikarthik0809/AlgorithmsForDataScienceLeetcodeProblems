class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num=int(n)
        mx_ln=int(log2(num))+1
        for i in range(mx_ln,1,-1):
            low=2
            high=num-1
            while low<=high:
                mid=(low+high)//2
                sm=0
                current=1
                for _ in range(i):
                    sm+=current
                    current*=mid
                if sm==num:
                    return str(mid)
                elif sm>num:
                    high=mid-1
                else:
                    low=mid+1
        return str(num-1)

        