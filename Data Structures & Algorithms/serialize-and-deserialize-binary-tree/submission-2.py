# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                nodes.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                nodes.append('.')
        
        print(nodes)
        return '-'.join(nodes)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split('-')

        if nodes[0] == '.':
            return None

        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()
            if i < len(nodes):
                if nodes[i] != '.':
                    node.left = TreeNode(int(nodes[i]))
                    q.append(node.left)
                i += 1
            if i < len(nodes):
                if nodes[i] != '.':
                    node.right = TreeNode(int(nodes[i]))
                    q.append(node.right)
                i += 1

        return root

