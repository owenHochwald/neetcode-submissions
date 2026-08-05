class FreqStack:

    def __init__(self):
        self.mx = 0
        self.lookup = defaultdict(list)
        self.counter = Counter()
        

    def push(self, val: int) -> None:
        self.counter[val] += 1
        f = self.counter[val]

        self.mx = max(self.mx, f)
        self.lookup[f].append(val)

    def pop(self) -> int:
        group = self.lookup[self.mx]
        end = group.pop()
        self.counter[end] -= 1
        

        if not self.lookup[self.mx]:
            self.mx -= 1
        return end



        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()