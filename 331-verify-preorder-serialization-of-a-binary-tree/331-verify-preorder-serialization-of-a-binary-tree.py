class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder, stack = preorder.split(","), []
        for item in preorder:
            # item is the character waiting to be operated
            # if topmost is # and item is #, this means we've reached some leaf
            # pop the topmost # and pop its next (replace fully visited leaf with #)
            while stack and item == stack[-1] == "#":
                stack.pop()
                if not stack:
                    return False
                stack.pop()
            stack.append(item)
        if stack == ["#"]:
            return True
        return False