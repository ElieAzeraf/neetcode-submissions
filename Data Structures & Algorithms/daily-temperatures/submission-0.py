class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        stack = []
        for idt, t in enumerate(temperatures):

            while len(stack) > 0 and t > stack[-1][0]:
                ans[stack[-1][1]] = idt - stack[-1][1]
                stack.pop()

            stack.append([t, idt])

        return ans

        