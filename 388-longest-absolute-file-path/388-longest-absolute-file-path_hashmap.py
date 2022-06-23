class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        s = input.split("\n")
        dic = {}
        longest = 0
        for path in s:
            if "." not in path:
                key = path.count("\t")
                dic[key] = len(path.replace("\t",""))
            else:
        # everytime see a file, parent key-value pairs have already been updated
                key = path.count("\t")
                path_len = sum([dic[j] for j in dic if j < key])
                path_len += key + len(path.replace("\t",""))
                longest = max(longest, path_len)
        return longest
