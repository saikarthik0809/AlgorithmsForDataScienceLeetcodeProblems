class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        visited = [False] * len(nums)

        def backtrack(currArr):
            if len(currArr) == len(nums):
                res.append(currArr.copy())
                return

            for index in range(len(nums)):
                if visited[index]:
                    continue
                
                if index > 0 and nums[index] == nums[index - 1] and not visited[index - 1]:
                    continue
                
                visited[index] = True
                currArr.append(nums[index])
                backtrack(currArr)
                currArr.pop()
                visited[index] = False
            
        backtrack([])
        return res