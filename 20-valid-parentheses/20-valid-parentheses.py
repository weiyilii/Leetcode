class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            else:
                if not stack or stack[-1] != hmap[c]:
                    return False
                stack.pop()
        return True if not stack else False