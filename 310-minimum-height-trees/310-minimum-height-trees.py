class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Given a valid tree, initialize the graph
        # Find centroids, which number <= 2
        # Otherwise, if 3 centroids, they must form a triangle, not valid
        if n <= 2:
            return [i for i in range(n)]
        
        graph = [set() for i in range(n)]
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        
        # Leaves: only have one egde, trim leaves out level by level
        # Each time get new leaves
        # Trim until <= 2 nodes left
        
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
                
        remain = n
        while remain > 2:
            remain -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                # set.pop() will remove a random element from the set
                # We make sure leaf's edge set has only one element
                i = graph[leaf].pop()
                # Trim
                graph[i].remove(leaf)
                # Check after triming, if it becomes a leaf
                if len(graph[i]) == 1:
                    new_leaves.append(i)
            leaves = new_leaves
        
        return leaves