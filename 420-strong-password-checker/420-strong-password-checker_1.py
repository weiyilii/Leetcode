class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        s = len(password)
        missing = 3
        if any("a" <= c <= "z" for c in password): missing -= 1
        if any("A" <= c <= "Z" for c in password): missing -= 1
        if any(c.isdigit() for c in password): missing -= 1
            
        i = 2
        change = 0
        one, two = 0, 0
        while i < s:
            if password[i] == password[i-1] == password[i-2]:
                length = 2
                while i < s and password[i] == password[i-1]:
                    i += 1
                    length += 1
                change += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                i += 1
        
        if s < 6:
            return max(6-s, missing)
        elif s <= 20:
            return max(change, missing)
        else:
            delete = s - 20
            change -= min(delete, one)
            change -= min(max(delete-one, 0), 2*two) // 2
            change -= max(delete-one-2*two, 0) // 3
            return delete + max(missing, change)
