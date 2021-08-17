class Solution(object):
    def groupAnagrams(self, strs):
        for i in range(len(strs)):
            j = strs[i][::-1]
            
        return strs



strs = ["eat","tea","tan","ate","nat","bat"]
a = Solution()
print(a.groupAnagrams(strs))