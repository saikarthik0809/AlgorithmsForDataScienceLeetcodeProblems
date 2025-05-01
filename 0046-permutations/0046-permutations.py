from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        permut = []

        def find_permutations(left_vals):
            if not left_vals:
                res.append(permut.copy())
                return             
            
            for i, n in enumerate(left_vals):
                permut.append(n)
                find_permutations(left_vals[:i] + left_vals[i + 1:])
                permut.pop()
            
        find_permutations(nums)

        return res