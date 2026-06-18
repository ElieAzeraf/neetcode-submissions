class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        inverse_hm = {o: [] for o in hm.values()}
        for n in hm.keys():
            inverse_hm[hm[n]].append(n)
        print(inverse_hm)

        sorted_occurences = sorted(list(inverse_hm.keys()), reverse=True)
        output = []

        for o in sorted_occurences[:k]:
            output += inverse_hm[o]
            if len(output) == k:
                break

        return output
        

        