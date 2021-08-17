class Solution(object):
    def __init__(self):
        self.romInt = {
            "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
            "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5,
            "IV": 4, "I": 1
        }
    def romanToInt(self, s): 
        result, i = 0, 0
        while i < len(s):
            try:
                result += self.romInt[s[i] + s[i+1]]
                i+=2
            except:
                result += self.romInt[s[i]]
                i+=1
        return result

a = Solution()
print(a.romanToInt("MCMXCIV"))