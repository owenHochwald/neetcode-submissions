class Node:
    def __init__(self, val):
        self.val = val
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.num_elem = 0
        self.capacity = k
        self.front: Optional[Node] = None
        self.back: Optional[Node] = None


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
             
            
        # increment num of occupied nodes
        self.num_elem += 1
        node = Node(value) 

        # link up this node to the old back of the list
        if self.back:
            node.next = self.back
            self.back.prev = node

        # advance the list with O(1) insert
        self.back = node

        # edge case when the back node is not set yet
        if not self.front:
            self.front = node # only need to set the node, don't need to link up, its itself!
        self.print_values()
        return True

    def print_values(self):
        curr = self.back
        for i in range(self.num_elem):
            if curr:
                print(curr.val)
                curr = curr.next
            else:
                break
        print('\n\n')
            

    def deQueue(self) -> bool:
        if self.isEmpty(): # there is nothing to pop
            return False
        
        # this is where we need to manage the back pointers
        self.num_elem -= 1

        if self.front == self.back: # pointer equivalance because they're the same element
            self.front = None
            self.back = None
            return True

        if self.front: # this line us just because of the strict type checker
            print("front of the queue is:", self.front.val)
            self.front = self.front.prev
            self.front.next = None # clear the Node to remove GC reference count

        # note that there is a case when the back == front
        return True
        
        

    def Front(self) -> int:
        return self.front.val if not self.isEmpty() and self.front else -1
        

    def Rear(self) -> int:
        return self.back.val if not self.isEmpty() and self.back else -1
        

    def isEmpty(self) -> bool:
        return self.num_elem == 0
        

    def isFull(self) -> bool:
        return self.num_elem == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()