class UF(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        self.parent[rootp] = rootq
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)
        dummy = 26
        for e in equations:
            if e[1] == "=":
                l1, l2 = ord(e[0]) - ord("a"), ord(e[3]) - ord("a")
                uf.union(l1, l2)
        for e in equations:
            if e[1] == "!":
                l1, l2 = ord(e[0]) - ord("a"), ord(e[3]) - ord("a")
                if uf.connected(l1, l2):
                    return False
        return True