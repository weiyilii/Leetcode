class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # Similar to solution_1
        # Modify courses to store taken courses, TLE
        
        courses.sort(key = lambda x: (x[1], x[0]))
        count = 0
        time = 0
        for i in range(len(courses)):
            if courses[i][0] + time <= courses[i][1]:
                time += courses[i][0]
                courses[count] = courses[i]
                count += 1
            else:
                max_i = i
                for j in range(count):
                    if courses[j][0] > courses[max_i][0]:
                        max_i = j
                if courses[max_i][0] > courses[i][0]:
                    time += courses[i][0] - courses[max_i][0]
                    courses[max_i] = courses[i]
        return count
