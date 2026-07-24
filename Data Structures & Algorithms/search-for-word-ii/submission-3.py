class Node:
    def __init__(self):
        self.children: dict[str, Node] = {} 
        self.terminal = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        out = []
        n, m = len(board), len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        # insert all of the words into the trie
        root = Node()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]
            curr.terminal = True

        out = []
        def dfs(i, j, node, seen, word):
            if node.terminal: 
                out.append(word)
                node.terminal = False
            
            seen.add((i, j))
            for dx, dy in dirs:
                x, y = dx + i, dy + j
                if 0 <= x < n and 0 <= y < m and (x, y) not in seen and board[x][y] in node.children:
                    dfs(x, y, node.children[board[x][y]], seen, word + board[x][y])
            seen.remove((i, j))

        for i in range(n):
            for j in range(m):
                if board[i][j] in root.children:
                    dfs(i, j, root.children[board[i][j]], set(), board[i][j])
        return out