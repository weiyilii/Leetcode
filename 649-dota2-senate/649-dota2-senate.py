class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        from collections import deque
        r, d = deque(), deque()
        n = len(senate)
        
        for i in range(n):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)
                
        while r and d:
            s1 = r.popleft()
            s2 = d.popleft()
            if s1 < s2:
                r.append(s1 + n)
            else:
                d.append(s2 + n)
        
        return "Radiant" if len(r) > len(d) else "Dire"