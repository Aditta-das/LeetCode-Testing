class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        rev_s = s[::-1]
        for i in range(len(s)-1):
            if s[0:n-i] == rev_s[i:]:
                return rev_s[:i] + s
        return rev_s[:-1] + s
s = "abcd"
a = Solution()
print(a.shortestPalindrome(s))