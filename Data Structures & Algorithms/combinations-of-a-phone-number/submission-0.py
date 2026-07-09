class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        path = []

        def dfs(path,n):
            if len(path) == len(digits) == 0:
                return []
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            if n < len(digits):
                for value in digitToChar[digits[n]]:
                    path.append(value)
                    dfs(path, n + 1)
                    path.pop()
                    
        dfs([], 0)
        return res
                
                    
