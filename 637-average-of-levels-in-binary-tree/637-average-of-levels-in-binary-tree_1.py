# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # DFS
        res = [0]
        count = [0]
        
        def avg(node, level):
            if not node:
                return
            if level < len(res):
                res[level] += node.val
                count[level] += 1
            else:
                res.append(node.val)
                count.append(1)
            avg(node.left, level + 1)
            avg(node.right, level + 1)
            
        avg(root, 0)
        for i in range(len(res)):
            res[i] = float(res[i])/count[i]
        return res
