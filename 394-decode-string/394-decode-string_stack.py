class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cur_num, cur_str, stack = 0, '', []
        for i in s:
            if i == "[":
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif i == ']':
                num = stack.pop()
                prev = stack.pop()
                cur_str = prev + num*cur_str
            elif i.isdigit():
                cur_num = cur_num*10 + int(i)
            else:
                cur_str += i
        return cur_str
