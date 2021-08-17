from typing import NewType


class Solution(object):
    def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
        new_sort = []
        for i in strs:
            new_sort.append(sorted(i))
        
        sort_word = ["".join(s) for s in new_sort]
        out_dict = dict()
        for idx, val in enumerate(sort_word):
            if val in out_dict:
                out_dict[val].append(strs[idx])
            else:
                out_dict[val] = [strs[idx]]
        return [out_dict[x] for x in out_dict]
            
#             print(strs[i])
#         return strs

strs = ["eat","tea","tan","ate","nat","bat"]
a = Solution()
print(a.groupAnagrams(strs))
