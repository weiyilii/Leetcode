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
        res, stack = [], [root]
        while stack:
            cur = stack.pop()
            if cur:
                stack.append(cur.right)
                stack.append(cur.left)
                res.append(cur.val)
        s = ','.join(map(str, res))
        return "[" + s + "]"
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:len(data)-1]
        if not data:
            return None
        data = map(int, data.split(','))
        root = TreeNode(data[0])
        i = 1
        while i < len(data):
            self.insert(data[i], root)
            i += 1
        return root
    
    def insert(self, value, root):
        if root:
            if root.left and root.right:
                if value > root.val:
                    self.insert(value, root.right)
                else:
                    self.insert(value, root.left)
            elif root.left:
                if value > root.val:
                    root.right = TreeNode(value)
                else:
                    self.insert(value, root.left)
            elif root.right:
                if value < root.val:
                    root.left = TreeNode(value)
                else:
                    self.insert(value, root.right)
            else:
                if value < root.val:
                    root.left = TreeNode(value)
                else:
                    root.right = TreeNode(value)
        return

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans