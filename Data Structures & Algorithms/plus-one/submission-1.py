class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = -1
        
        while -i <= len(digits) and digits[i] == 9:
            digits[i] = 0
            i -= 1

        if -i <= len(digits):
            digits[i] = digits[i] + 1
        else:
            digits = [1] + digits

        return digits
        