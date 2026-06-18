class Solution:
    def maxArea(self, heights: List[int]) -> int:

        def compute_water_amount(b, e):
            return min(heights[b], heights[e]) * (e - b)

        b, e = 0, len(heights) - 1
        ans = compute_water_amount(b, e)

        while b != e:
            if heights[b] <= heights[e]:
                b += 1
            else:
                e -= 1
            ans = max(ans, compute_water_amount(b, e))

        return ans






        

        


