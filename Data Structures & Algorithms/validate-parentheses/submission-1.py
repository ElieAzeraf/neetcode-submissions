class Solution:
    def isValid(self, s: str) -> bool:

        hm = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        open_set = set(["(", "{", "["])

        stack = []

        for c in s:
            if c in hm:
                if len(stack) == 0 or stack[-1] != hm[c]:
                    return False
                else:
                    stack.pop()

            if c in open_set:
                stack.append(c)

        if stack == []:
            return True

        return False

        