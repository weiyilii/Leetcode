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
        def dfs_s(node):
            if node:
                vals.append(str(node.val))
                dfs_s(node.left)
                dfs_s(node.right)
            else:
                vals.append('#')
        vals = []
        dfs_s(root)
        res = ' '.join(vals)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs_d():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = dfs_d()
                node.right = dfs_d()
            return node
                
        data = data.split(' ')
        vals = iter(data)
        res = dfs_d()
        return res

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))