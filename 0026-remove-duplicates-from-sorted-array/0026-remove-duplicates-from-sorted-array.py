class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = 0

        if not nums:
            return 0

        for r in range(len(nums)):
            if nums[l] != nums[r]:

                l += 1
                nums[l] = nums[r]

        return l + 1