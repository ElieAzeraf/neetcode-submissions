class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        b, e = 0, len(numbers) - 1

        while numbers[b] + numbers[e] != target:

            if numbers[b] + numbers[e] > target:
                e -= 1
            else:
                b += 1

        return [b + 1, e + 1]


        