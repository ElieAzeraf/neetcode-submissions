class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_product = 1
        zero_number, zero_index = 0, -1
        for idn, n in enumerate(nums):
            if n == 0:
                zero_number += 1
                if zero_number == 2:
                    return [0] * len(nums)
                zero_index = idn
            else:
                total_product *= n
        
        if zero_number == 1:
            ans = [0] * len(nums)
            ans[zero_index] = total_product
            return ans

        ans = [total_product] * len(nums)
        for idn, n in enumerate(nums):
            ans[idn] = int(ans[idn]/n)
        
        return ans

        
            

        