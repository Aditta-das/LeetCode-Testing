from typing import Counter


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        s = strs[0]
        for i in range(len(strs)):
            temp = ""
            if len(s) == 0:
                break
            for j in range(len(strs[i])):
                if j < len(s) and (s[j] == strs[i][j]):
                    temp += s[j]
                else:
                    break
            s = temp
        return s


strs = ["aaa","aa","aaa"]
a = Solution()
print(a.longestCommonPrefix(strs))