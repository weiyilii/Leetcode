# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        if not root:
            return ''
        q = deque()
        q.append(root)
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('#')
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        from collections import deque
        if data == '':
            return None
        data = data.split()
        root = TreeNode(int(data[0]))
        q = deque()
        q.append(root)
        
        i = 1
        while i < len(data):
            parent = q.popleft()
            if data[i] != '#':
                left = TreeNode(int(data[i]))
                parent.left = left
                q.append(left)
            i += 1
            if data[i] != '#':
                right = TreeNode(int(data[i]))
                parent.right = right
                q.append(right)
            i += 1
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))