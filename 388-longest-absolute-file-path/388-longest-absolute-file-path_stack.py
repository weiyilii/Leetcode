class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # Using stack, each element in stack = length of the path to this element
        # kinda like DFS, track length for each level
        stack = []
        longest = 0
        s = input.split("\n")
        for path in s:
            plen = len(path.lstrip("\t"))
            level = len(path)-plen
            while stack and level < len(stack):
                stack.pop()   
            if not stack:
                stack.append(plen)
            else:
                stack.append(plen + stack[-1])
            if "." in path:
                longest = max(longest, stack[-1]+len(stack)-1)
        return longest
