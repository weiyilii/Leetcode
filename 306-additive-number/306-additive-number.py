class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        if n < 3:
            return False
        
        def dfs(n1, n2, k):
            if k == n-1:
                return True
            for t in range(k+1, n):
                new = num[k+1:t+1]
                n3 = int(new)
                if (new == "0" or new[0] != "0") and n3 == n1 + n2:
                    if dfs(n2, n3, t):
                        return True
            return False
        
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                n1, n2 = num[:i+1], num[i+1:j+1]
                if (n1 == "0" or n1[0] != "0") and (n2 == "0" or n2[0] != "0"):
                    if dfs(int(n1), int(n2), j):
                        return True
        return False