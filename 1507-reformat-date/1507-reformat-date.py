class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        s = date.split(" ")
        year = s[2]
        m = {"Jan": "01", 
             "Feb": "02",
             "Mar": "03", 
             "Apr": "04", 
             "May": "05", 
             "Jun": "06", 
             "Jul": "07", 
             "Aug": "08", 
             "Sep": "09", 
             "Oct": "10", 
             "Nov": "11", 
             "Dec": "12"}
        month = m[s[1]]
        if len(s[0]) == 3:
            day = "0" + s[0][0]
        else:
            day = s[0][:2]
        return year + "-" + month + "-" + day