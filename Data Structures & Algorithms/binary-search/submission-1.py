class Solution:
    def search(self, nums: List[int], target: int) -> int:

        b, e = 0, len(nums) - 1

        for i in range(4):

            m = (e + b) // 2

            if nums[m] == target:
                return m

            elif nums[m] < target:
                b = m + 1
            else:
                e = m - 1

        return -1
        