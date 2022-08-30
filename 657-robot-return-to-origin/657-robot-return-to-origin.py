class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for m in moves:
            if m == "R":
                x += 1
            elif m == "L":
                x -= 1
            elif m == "U":
                y += 1
            else:
                y -= 1
        return x == 0 and y == 0