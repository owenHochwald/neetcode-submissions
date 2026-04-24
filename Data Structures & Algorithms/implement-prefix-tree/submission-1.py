class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.terminal = False


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        temp = self.root
        for c in word:
            temp = temp.children[c]
        temp.terminal = True


    def search(self, word: str) -> bool:
        temp = self.root
        for c in word:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return temp.terminal
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for c in prefix:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return True
        
        