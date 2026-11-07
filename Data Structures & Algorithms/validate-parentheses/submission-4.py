class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        stack = []

        for c in s:
                
            if c in [')', ']', '}']:
                if len(stack) == 0:
                    return False

                prev = stack.pop()

                if prev == '(' and c!=')':
                    return False
                elif prev == '{' and c!='}':
                    return False
                elif prev == '[' and c!=']':
                    return False
            else:
                stack.append(c)

        if len(stack) != 0:
            return False
            
        return True