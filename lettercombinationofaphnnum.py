class Solution(object):
    def letterCombinations(self, digits):
        pd = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(pd[digits[0]])
        p = self.letterCombinations(digits[:-1])
        ad = pd[digits[-1]]
        return[s+c for s in p for c in ad]


digits = "23"
a = Solution()
print(a.letterCombinations(digits))