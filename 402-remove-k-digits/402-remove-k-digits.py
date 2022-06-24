class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in num:
            while stack and k and stack[-1] > i:
                stack.pop()
                k -= 1
            if stack or i != '0':
                stack.append(i)
        if k:
            stack = stack[0:-k]
            
        res = ''.join(stack)
        
        return res if res else '0'