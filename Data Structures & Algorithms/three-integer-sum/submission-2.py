class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        hm = {}
        for id1, n1 in enumerate(nums):
            for id2, n2 in enumerate(nums[id1 + 1:]):
                if sorted([n1, n2]) not in hm.get(-n1-n2, []):
                    hm[- n1 - n2] = hm.get(-n1-n2, []) + [[id1, id2 + id1 + 1]]

        ans = []
        for idn, n in enumerate(nums):
            if n in hm:
                for ids in hm[n]:
                    candidate = sorted([nums[ids[0]], 
                                    nums[ids[1]],
                                    nums[idn]])
                    if idn not in ids and candidate not in ans:
                        ans.append(candidate)
        
        return ans
        