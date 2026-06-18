class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_hm = {num: [] for num in nums}
        for idn, num in enumerate(nums):
            nums_hm[num].append(idn)

        for idn, num in enumerate(nums):
            if target - num in nums_hm:
                if nums_hm[target - num][-1] != idn:
                    return [idn, nums_hm[target - num][-1]]

        
        