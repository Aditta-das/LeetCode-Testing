class Solution(object):
    def groupAnagrams(self, strs):
        output = []
        for str in strs:
            output.append(sorted(str))
        sort_word = [''.join(s) for s in output]
        out_dict = {}
        for idx, val in enumerate(sort_word):
            if val in out_dict:
                out_dict[val].append(strs[idx])
            else:
                out_dict[val] = [strs[idx]]
        return [out_dict[x] for x in out_dict]


strs = [""]
a = Solution()
print(a.groupAnagrams(strs))