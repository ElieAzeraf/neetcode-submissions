class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        memo = [None] * len(nums)

        memo[-1] = nums[-1]
        memo[-2] = max(nums[-1], nums[-2])

        idn = -3
        while -idn <= len(nums):
            memo[idn] = max(nums[idn] + memo[idn + 2], memo[idn + 1])
            idn -= 1

        return memo[0]
        
        