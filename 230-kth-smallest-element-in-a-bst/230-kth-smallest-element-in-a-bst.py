# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        i = 0 # count variable
        cur = root
        # Inorder traversal using stack
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            # elements will be poped out ascendingly
            # when i reaches k, kth smallest element is being poped out
            i += 1
            if i == k:
                return cur.val
            cur = cur.right