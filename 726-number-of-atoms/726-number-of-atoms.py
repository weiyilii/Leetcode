class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [dict()]
            
        i = 0
        while i < len(formula):
            c = formula[i]
            if c == "(":
                stack.append(dict())
                i += 1
            elif c == ")":
                top = stack.pop()
                i += 1
                i_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                multiple = int(formula[i_start:i]) if i > i_start else 1
                for name, count in top.items():
                    if name in stack[-1]:
                        stack[-1][name] += multiple*count
                    else:
                        stack[-1][name] = multiple*count
            else:
                i_start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                name = formula[i_start:i]
                i_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i]) if i > i_start else 1
                if name in stack[-1]:
                    stack[-1][name] += count
                else:
                    stack[-1][name] = count
        
        res = ''
        for name in sorted(stack[-1]):
            count = stack[-1][name]
            res += name
            if count > 1:
                res += str(stack[-1][name])
        return res
                