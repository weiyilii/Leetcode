# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            l = len(q)
            curMax = float('-inf')
            for _ in range(l):
                node = q.popleft()
                curMax = max(curMax, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(curMax)
        return res