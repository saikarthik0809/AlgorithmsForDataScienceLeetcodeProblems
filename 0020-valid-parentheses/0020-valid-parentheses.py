class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for bracket in s:
            if bracket in bracket_map.values():
                stack.append(bracket)
            else : # closed bracket; pop off 
                if not stack or bracket_map[bracket] != stack.pop():
                    return False
        if stack: 
            return False
        return True