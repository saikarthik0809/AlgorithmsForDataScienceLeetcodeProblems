class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtracking(opened_count, closed_count, s):
            if len(s) == n * 2:
                result.append(s)
                return
            
            if opened_count < n:
                backtracking(opened_count + 1, closed_count, s + "(")
            
            if opened_count > closed_count:
                backtracking(opened_count, closed_count + 1, s + ")")
        
        backtracking(0, 0, "")

        return result