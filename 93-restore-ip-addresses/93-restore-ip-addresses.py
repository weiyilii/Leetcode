class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        
        def dfs(path, prev):
            if len(path) == 4 and prev == len(s) - 1:
                ip = ".".join(path)
                res.append(ip)
                return
            for j in range(prev+1, prev+4):
                if j < len(s):
                    new = s[prev+1:j+1]
                    if new == '0' or (new[0] != '0' and int(new) <= 255):
                        dfs(path + [new], j)
        
        dfs([], -1)
        return res