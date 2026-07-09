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

        def dfs(path, i):
            if len(path) == len(digits):
                res.append(path)
                return
            
           
            for value in digitToChar[digits[i]]:
                path += value
                dfs(path, i + 1)
                path = path[: -1]
        if digits:
            dfs("", 0)
        return res
                
                    
