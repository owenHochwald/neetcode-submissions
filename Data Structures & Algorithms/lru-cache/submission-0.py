class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val  
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.chain = None
        self.capacity = capacity
        
        self.left, self.right = Node(0, 0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        

    def get(self, key: int) -> int:
        if key in self.lru:
            self.remove(self.lru[key])
            self.insert(self.lru[key])
            return self.lru[key].val
        return -1

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.remove(self.lru[key])
        self.lru[key] = Node(key, value)
        self.insert(self.lru[key])

        if len(self.lru) > self.capacity:
            lruNode = self.left.next
            self.remove(lruNode)
            del self.lru[lruNode.key]
        


        
