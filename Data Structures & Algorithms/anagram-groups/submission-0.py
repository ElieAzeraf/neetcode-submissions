class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}
        for s in strs:
            hm[s] = {}
            for c in s:
                hm[s][c] = hm[s].get(c, 0) + 1

        output = [[strs[0]]]
        for s in strs[1:]:
            has_anagram = False
            for ido, o in enumerate(output):
                if hm[s] == hm[o[0]]:
                    output[ido].append(s)
                    has_anagram = True
                    break

            if not has_anagram:
                output.append([s])

        return output
            
        