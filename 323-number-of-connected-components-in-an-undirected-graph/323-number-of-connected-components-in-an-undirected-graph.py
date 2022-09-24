class UF(object):
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        self.parent[rootq] = rootp
        self.count -= 1
        
    def connected(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        return rootp == rootq
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for [p, q] in edges:
            uf.union(p, q)
        return uf.count