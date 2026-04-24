class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # prechecking conditions
        if endWord not in wordList or len(beginWord) != len(endWord):
            return 0

        wordSet = set(wordList)

        # function to efficiently generate neighbors
        def generate_neighbors(word):
            neighbors = []
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != word[i]:
                        curr = word[:i] + c + word[i+1:]
                        if curr in wordSet:
                            neighbors.append(curr)
            return neighbors

        # BFS to find shortest hops from the start, generating neighbors on the fly
        q = deque()
        seen = set()

        q.append([beginWord, 0])

        while q:
            # check to make sure we aren't just going around in cycles
            node, hops = q.popleft()

            if hops > len(wordList):
                return 0

            if node not in seen:

                neighbors = generate_neighbors(node)
                seen.add(node)

                for n in neighbors:
                    if n == endWord:
                        return hops + 2
                    q.append([n, hops+1])
        return 0
          
                    
                
            


        

        

        