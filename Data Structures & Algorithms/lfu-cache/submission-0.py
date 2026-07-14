from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict(OrderedDict) # each key maps to a frequency
        self.lookup = {}
        self.cap = capacity
        self.min_freq = 0
        

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1

        freq = self.lookup[key] 
        self.lookup[key] += 1

        val = self.cache[freq][key]
        self.cache[freq].pop(key)
        
        if freq == self.min_freq and not self.cache[freq]:
            self.min_freq += 1
        
        self.cache[freq + 1][key] = val
        self.cache[freq+1].move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        # check if it is present
        if self.get(key) != -1:
            freq = self.lookup[key]
            self.cache[freq][key] = value
            return

        if len(self.lookup) == self.cap:
            e_key, _ = self.cache[self.min_freq].popitem(last=False)
            del self.lookup[e_key]

        # frequency starts with 1
        self.cache[1][key] = value
        self.lookup[key] = 1
        self.cache[1].move_to_end(key)
        self.min_freq = 1


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)