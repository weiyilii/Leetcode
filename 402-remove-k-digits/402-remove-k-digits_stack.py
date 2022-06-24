class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # Monotonic Stack
        stack = []
        for i in num:
            # usual: append every digit
            # however, when top element is larger than i, pop top out
            # update k, meaning we only have k-1 chances now to pop element and not keep it in result
            while stack and k and stack[-1] > i:
                stack.pop()
                k -= 1
            if stack or i != '0':
                stack.append(i)
        # if previous digits are pretty well ascending, we dont get a change to leave elements out
        # k is not fully consumed
        # in this case just cut last k elements from stack
        if k:
            stack = stack[0:-k]
            
        res = ''.join(stack)
        
        return res if res else '0'
