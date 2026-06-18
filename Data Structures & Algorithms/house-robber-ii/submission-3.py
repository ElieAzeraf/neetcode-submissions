class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 3:
            return max(nums)

        memo_1 = [None] * len(nums)

        memo_1[-1] = nums[-1]
        memo_1[-2] = max(nums[-2], nums[-1])

        idn = -3
        while -idn < len(nums):
            memo_1[idn] = max(memo_1[idn + 1], nums[idn] + memo_1[idn + 2])
            idn -= 1


        memo_2 = [None] * len(nums)
        memo_2[-2] = nums[-2]
        memo_2[-3] = max(nums[-2], nums[-3])

        idn = -4
        while -idn <= len(nums):
            memo_2[idn] = max(memo_2[idn + 1], nums[idn] + memo_2[idn + 2])
            idn -= 1

        return max(memo_1[1], memo_2[0])
        
        
        