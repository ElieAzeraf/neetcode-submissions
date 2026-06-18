class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hm = {}
        for c in s:
            hm[c] = hm.get(c, 0) + 1

        for c in t:
            hm[c] = hm.get(c, 0) - 1
            if hm[c] < 0:
                return False

        for c in hm:
            if hm[c] != 0:
                return False

        return True
        