class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key = lambda x: (x[1], x[0]))
        time = 0
        valid_list = []
        for i in range(len(courses)):
            if courses[i][0] + time <= courses[i][1]:
                time += courses[i][0]
                valid_list.append(courses[i][0])
            else:
                max_j = 0
                for j in range(1, len(valid_list)):
                    if valid_list[j] > valid_list[max_j]:
                        max_j = j
                if max_j < len(valid_list) and valid_list[max_j] > courses[i][0]:
                    time += courses[i][0] - valid_list[max_j]
                    valid_list[max_j] = courses[i][0]
        return len(valid_list)