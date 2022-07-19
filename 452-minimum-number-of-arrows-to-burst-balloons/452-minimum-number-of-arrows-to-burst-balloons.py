class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: (x[0], x[1]))
        (left, right) = points[0]
        res = 1
        
        for i in range(1, len(points)):
            if points[i][0] > right:
                res += 1
                (left, right) = points[i]
            else:
                left = points[i][0]
                right = min(right, points[i][1])
        
        return res