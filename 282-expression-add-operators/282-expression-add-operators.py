class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        l = len(num)
        res = []
        
        def dfs(value, number, prev, exp):
            if prev == l-1:
                if value == target:
                    print(value)
                    res.append(exp)
                return
            for i in range(prev+1, l):
                new_s = num[prev+1:i+1]
                if new_s == "0" or new_s[0] != "0":
                    n = int(new_s)
                    dfs(value + n, n, i, exp + "+" + new_s)
                    dfs(value - n, -n, i, exp + "-" + new_s)
                    dfs(value - number + number*n, number*n, i, exp + "*" + new_s)
        
        for i in range(0, l):
            s = num[:i+1]
            if s == "0" or s[0] != "0":
                number = int(s)
                dfs(number, number, i, s)
        return res