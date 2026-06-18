class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        p1, p2 = 0, 0
        seen_characters = set()
        ans = 0

        while p2 < len(s):

            if s[p2] not in seen_characters:
                seen_characters.add(s[p2])
                p2 += 1
                ans = max(ans, p2 - p1)

            else:
                seen_characters.remove(s[p1])
                p1 += 1
        

        return ans

        