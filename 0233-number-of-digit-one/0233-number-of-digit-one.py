class Solution:
    def countDigitOne(self, n: int) -> int:
        digits = list(map(int, str(n)))
        print(digits)
        
        @cache
        def dp(pos: int, tight: bool, count_ones: int) -> int:
            if pos == len(digits): return count_ones
            bound = digits[pos] if tight else 10
            res = 0
            for i in range(bound + 1):
                if i == 10: continue
                if i == 1:
                    if i < bound: res += dp(pos + 1, False, count_ones + 1)
                    elif i == bound: res += dp(pos + 1, True, count_ones + 1)
                else:
                    if i < bound: res += dp(pos + 1, False, count_ones)
                    elif i == bound: res += dp(pos + 1, True, count_ones)
            return res
        
        return dp(0, True, 0)