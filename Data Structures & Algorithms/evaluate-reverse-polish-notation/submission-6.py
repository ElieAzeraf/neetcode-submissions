class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        s = []
        for t in tokens:

            if t not in ["+", "-", "*", "/"]:
                s.append(int(t))
            else:
                i, j = s[-2], s[-1]
                s.pop()
                s.pop()
                if t == "+":
                    s += [i + j]
                elif t == "-":
                    s += [i - j]
                elif t == "*":
                    s += [i * j]
                elif t == "/":
                    s += [int(i / j)]

        return s[0]