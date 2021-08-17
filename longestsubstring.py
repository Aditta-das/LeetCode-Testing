class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = ''
        mx = 0
        for a in s:
            if a not in b:
                b+=a
                # print(b)
            else:
                b = b[b.index(a)+1:]+a
                print(b)
            mx = max(mx, len(b))
            # print(mx)
        return mx

s = "abcabcbb"
a = Solution()
print(a.lengthOfLongestSubstring(s))