class Solution:
    def mostBooked(self, n: int, m: List[List[int]]) -> int:
        return [a:=[*range(n)],o:=[],c:=[0]*n] and \
            [[next(1 for _ in count() if not (o and o[0][0]<=s and not heappush(a,heappop(o)[1]))),heappush(o,a and [e,r:=heappop(a)] or [o[0][0]+e-s,r:=heappop(o)[1]]),setitem(c,r,c[r]+1)] for s,e in sorted(m)] and \
            c.index(max(c))