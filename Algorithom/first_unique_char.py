class Solution(object):
    def firstUniqChar(self, s):
        dict = {}
        for w in s:
            if w not in dict:
                dict[w] = 1
            else:
                dict[w] += 1
        idx = -1
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1
        

s = "leetcode"
a = Solution()
print(a.firstUniqChar(s))