class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        p1, p2 = 0, 1
        ans = 0

        while p2 < len(prices):
            if prices[p1] >= prices[p2]:
                p1 = p2
                p2 = p1 + 1

            else:
                ans = max(ans, prices[p2] - prices[p1])
                p2 += 1

        return ans