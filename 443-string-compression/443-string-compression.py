class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left = 0
        char, count = chars[0], 0
        for c in chars:
            if c == char:
                count += 1
            else:
                if count == 1:
                    chars[left] = char
                    left += 1
                else:
                    chars[left] = char
                    left += 1
                    for n in str(count):
                        chars[left] = n
                        left += 1
                char = c
                count = 1
        if count == 1:
            chars[left] = c
            left += 1
        else:
            chars[left] = c
            left += 1
            for n in str(count):
                chars[left] = n
                left += 1
        return left