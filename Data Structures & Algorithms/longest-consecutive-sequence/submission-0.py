class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        max_length = 0

        already_seen = set()
        for n in nums:
            length = 1
            following_n = n + 1
            while following_n in nums_set:
                following_n += 1
                length += 1
            
            max_length = max(max_length, length)

        return max_length

        