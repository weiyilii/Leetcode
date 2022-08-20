# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        serial = collections.defaultdict(list)
        
        def dfs(node):
            if not node:
                return "#"
            preorder = str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)
            serial[preorder].append(node)
            return preorder
        
        dfs(root)
        for key in serial:
            if len(serial[key]) > 1:
                res.append(serial[key][0])
        return res