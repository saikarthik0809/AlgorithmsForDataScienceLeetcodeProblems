class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        n = len(nums)
        if n == k:
            return l

        ans = 0
        while l <= r:
            m = (l + r) // 2
            temp_sum = 0
            cnt = 0
            for num in nums:
                if temp_sum + num <= m:
                    temp_sum += num
                else:
                    cnt += 1
                    temp_sum = num
            cnt += 1

            if cnt <= k:
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans