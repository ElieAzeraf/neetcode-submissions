class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_values) == 0:
            self.min_values.append(val)
        else:
            self.min_values.append(min(val, self.min_values[-1]))

    def pop(self) -> None:
        del self.stack[-1]
        del self.min_values[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]

        
