# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/1208004/Extremely-Intuitive-O(1)-Space-solution-with-Simple-explanation-Python
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            # if cur has left child, find the right most node in left sub tree (prev)
            # shift cur's right sub tree to the right child of prev
            # shift cur's left sub tree to the right, left to None
            # move forward cur to cur.right
            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right
                prev.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
            
