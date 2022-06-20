class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        res = ""
        path = path.split("/")
        for d in path:
            if d == "":
                continue
            if d == "..":
                if stack:
                    stack.pop()
            elif d == ".":
                continue
            else:
                stack.append("/" + d)
        return "".join(stack) if len(stack) > 0 else "/"