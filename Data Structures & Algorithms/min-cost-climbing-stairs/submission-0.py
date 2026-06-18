class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [None] * len(cost)
        memo[-1] = cost[-1]
        memo[-2] = cost[-2]

        idc = -3
        while -idc <= len(cost):
            memo[idc] = cost[idc] + min(memo[idc + 1], memo[idc + 2])
            idc -= 1

        return min(memo[0], memo[1])