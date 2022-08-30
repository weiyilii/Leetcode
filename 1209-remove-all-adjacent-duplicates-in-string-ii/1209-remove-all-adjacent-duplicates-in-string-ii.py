class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack.append((c, stack[-1][1] + 1))
            else:
                stack.append((c, 1))
            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
        res = ""
        for pair in stack:
            res += pair[0]
        return res