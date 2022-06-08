# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(1, n)
    
    def helper(self, start, end):
        if start > end:
            return [None]
        
        all_trees = []
        for cur_root_val in range(start, end+1):
            all_left = self.helper(start, cur_root_val-1)
            all_right = self.helper(cur_root_val+1, end)
            for left_tree in all_left:
                for right_tree in all_right:
                    cur_root = TreeNode(cur_root_val)
                    cur_root.left = left_tree
                    cur_root.right = right_tree
                    all_trees.append(cur_root)
        return all_trees