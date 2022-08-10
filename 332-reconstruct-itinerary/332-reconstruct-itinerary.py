class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        for [src, dst] in tickets:
            graph[src].append(dst)
        for key in graph:
            graph[key].sort(reverse = True)
        
        stack = ["JFK"]
        res = []
        while stack:
            elem = stack[-1]
            if elem in graph and len(graph[elem]) > 0:
                stack.append(graph[elem].pop())
            else:
                res.append(stack.pop())
        return res[::-1]