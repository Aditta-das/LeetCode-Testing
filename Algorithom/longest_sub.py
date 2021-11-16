class Solution:
    def lengthOfLongestSubstring(self, s):
        not_seen = {}
        start = 0
        longest = 0
        if len(s) == 0:
            return 0
            
        for i, a in enumerate(s):
            if a in not_seen:
                start = max(start, not_seen[a]+1)
            longest = max(longest, i-start+1)
            not_seen[a] = i
        return longest


s = 'pwwkew'
a = Solution()
print(a.lengthOfLongestSubstring(s))