class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # Time: n^2
        # space: 1
        # Time Limit Exceeds
        
        courses.sort(key = lambda x: (x[1], x[0]))
        count = 0
        time = 0
        for i in range(len(courses)):
            if courses[i][0] + time <= courses[i][1]:
                count += 1
                time += courses[i][0]
            else:
                max_i = i
                for j in range(i):
                    if courses[j][0] > courses[max_i][0]:
                        max_i = j
                if courses[max_i][0] > courses[i][0]:
                    time += courses[i][0] - courses[max_i][0]
                courses[max_i][0] = -1
        return count
