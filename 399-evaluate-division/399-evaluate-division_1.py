class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(dict)
        for eq, value in zip(equations, values):
            a, b = eq[0], eq[1]
            graph[a][b] = value
            graph[b][a] = 1/value
        
        def dfs(cur, goal, val):
            if cur == goal:
                return val
            for new_cur in graph[cur]:
                if new_cur not in seen:
                    seen.add(new_cur)
                    res = dfs(new_cur, goal, val*graph[cur][new_cur])
                    if res != -1:
                        return res
                    seen.remove(new_cur)
            return -1
        
        res = []
        for cur, goal in queries:
            if cur not in graph or goal not in graph:
                res.append(-1)
            else:
                seen = set()
                res.append(dfs(cur, goal, 1.0))
        return res
