class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [1, 2, 3]

        while len(memo) < n:
            memo.append(memo[-2] + memo[-1])

        return memo[n - 1]
        