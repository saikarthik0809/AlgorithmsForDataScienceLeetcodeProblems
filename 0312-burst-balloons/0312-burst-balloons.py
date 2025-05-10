class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dptable = {}

        def dfs(l, r):
            if l > r: return 0
            elif (l, r) in dptable: return dptable[(l, r)]
            
            lside = nums[l - 1]
            rside = nums[r + 1]
            
            dptable[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[i] * lside * rside
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dptable[(l, r)] = max(dptable[(l, r)], coins)
            
            return dptable[(l, r)]
            
        return dfs(1, len(nums) - 2)