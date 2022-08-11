# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.seen = collections.defaultdict(int)
        self.dfs(root)
        freq, res = float('-inf'), []
        for key in self.seen:
            if self.seen[key] > freq:
                res = [key]
                freq = self.seen[key]
            elif self.seen[key] == freq:
                res.append(key)
        return res
    
    def dfs(self, root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        curSum = left + right + root.val
        self.seen[curSum] += 1
        return curSum