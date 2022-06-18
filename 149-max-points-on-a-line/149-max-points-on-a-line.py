class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """       
        def slope(p1, p2):
            
            def gcd(a, b):
                if b == 0:
                    return a
                return gcd(b, a%b)
            
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0:
                return 'v'
            elif dy == 0:
                return 'h'
            else:
                return (dx/gcd(dx, dy), dy/gcd(dx, dy))
        
        res = 1
        
        while points:
            cur = points.pop()
            dic = collections.defaultdict(int)
            duplicates = 0
            for point in points:
                if cur[0] == point[0] and cur[1] == point[1]:
                    duplicates += 1
                else:
                    s = slope(cur, point)
                    dic[s] += 1
            if dic:
                res = max(res, max(dic.values()) + duplicates + 1)
            
        return res
        