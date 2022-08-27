class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y, d = 0, 0, 0
        for i in instructions:
            if i == "L":
                d = (d - 1) % 4
            elif i == "R":
                d = (d + 1) % 4
            else:
                if d == 0:
                    y += 1
                elif d == 1:
                    x += 1
                elif d == 2:
                    y -= 1
                else:
                    x -= 1
        if (d != 0) or (x == 0 and y == 0):
            return True
        else:
            return False