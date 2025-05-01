import math

class Solution:
    res = []
    def getPermutation(self, n: int, k: int) -> str:
        self.res = []
        arr = [i for i in range(1, n+1)]
        if n == 1:
            return str(n)
        self.getPermutationRec(arr, k)
        return ''.join([str(i) for i in self.res])


    def getPermutationRec(self, arr, n):
        if n == 0:
            self.res.extend(list(arr))
            return
        if len(arr) == 2:
            if n == 1:
                self.res.extend(list(arr))
                return
            self.res.extend(list(arr[::-1]))
            return
        lenn = len(arr)
        perms = math.factorial(lenn-1)
        cur_perm = 0
        i = 0
        while i < lenn - 1:
            if cur_perm + perms >= n:
                break
            i+=1
            cur_perm += perms
        self.res.append(arr[i])
        self.getPermutationRec(arr[:i]+arr[i+1:], n - cur_perm)

        