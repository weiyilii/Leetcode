class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_t, t_s = {}, {}
        for i in range(len(s)):
            si, ti = s[i], t[i]
            if si in s_t:
                if s_t[si] != ti:
                    return False
            else:
                s_t[si] = ti
            if ti in t_s:
                if t_s[ti] != si:
                    return False
            else:
                t_s[ti] = si
        return True