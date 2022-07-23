class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # Use a max heap to track the durations of courses taken
        # Anytime give the max duration
        
        from heapq import heappush, heappop
        courses.sort(key = lambda x: (x[1], x[0]))
        time = 0
        h = []
        for c in courses:
            if c[0] + time <= c[1]:
                time += c[0]
                heappush(h, -c[0])
            else:
                if h and -h[0] > c[0]:
                    time += heappop(h) + c[0]
                    heappush(h, -c[0])
        return len(h)
