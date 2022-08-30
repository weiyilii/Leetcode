class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        q = collections.deque([i for i in range(1, n+1)])
        while len(q) > 1:
            for _ in range(k-1):
                p = q.popleft()
                q.append(p)
            q.popleft()
        return q[0]
        