class MinStack:

    def __init__(self):
        self.s = []
        self.smin = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.smin:
            self.smin.append(min(val, self.smin[-1]))
        else:
            self.smin.append(val)
        

    def pop(self) -> None:
        self.s.pop()
        self.smin.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.smin[-1]
